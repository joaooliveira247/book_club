from book_club.core.crud import (
    insert_db,
    create_db,
    select_db,
    num_rows,
    delete_db,
)
from book_club.scraping.scraping import get_url_by_category, get_book
from book_club.models.book_model import BookModel
from book_club.core.config import settings
from book_club.utils import to_csv
from typer import Typer, Option
from rich.table import Table, Row
from rich.console import Console
from typing import Annotated

app = Typer()


@app.command()
def create():
    create_db()
    return


@app.command()
def load(
    csv: bool = False,
    path: Annotated[str, Option(..., help="path to directory")] = str(
        settings.BASE_DIR
    ),
):
    for category, url in get_url_by_category():
        if csv:
            to_csv(get_book(url, category), path)
            continue
        insert_db(get_book(url, category))
    return


@app.command()
def select(ids: list[int]):
    console = Console()
    book_table = Table(
        "ID",
        "Title",
        "Category",
        "Stars",
        "Price",
        "Available",
        title="Books",
    )

    def __add_rows(books: BookModel, table: Table) -> Row:
        table.add_row(
            str(books.id),
            books.title,
            books.category,
            str(books.stars),
            str(books.price),
            str(books.is_available),
        )
        return

    match len(ids):
        case _ if len(ids) > 0:
            for book in select_db(ids):
                print(type(book))
                __add_rows(book, book_table)
            console.print(book_table)
            return
        case _:
            console.print("Find another method.")
            return


@app.command()
def delete(id: int) -> None:
    operation = delete_db(id)
    if operation:
        print(f"Book in id: {id} deleted")
        return
    print(f"{id} not found.")


@app.command()
def rows():
    print(f"{num_rows()} Rows.")
