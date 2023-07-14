from book_club.core.crud import (
    insert_db,
    create_db,
    select_db,
    select_db_by_name,
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
from rich.theme import Theme
from typing import Annotated

app = Typer()

console = Console(
    theme=Theme(
        {"info": "dim cyan", "warning": "magenta", "danger": "bold red"}
    )
)

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


@app.command()
def create():
    msg = create_db()

    console.print(msg, style="info")
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
    match len(ids):
        case _ if len(ids) > 0:
            for book in select_db(ids):
                print(type(book))
                __add_rows(book, book_table)
            console.print(book_table)
            return
        case _:
            console.print("Find another method.", style="warning")
            return


@app.command()
def delete(id: int) -> None:
    operation = delete_db(id)
    if operation:
        console.print(f"Book in id: {id} deleted", style="info")
        return
    console.print(f"{id} not found.", style="warning")


@app.command()
def insert(
    book_title: str,
    category: str,
    stars: int,
    price: float,
    is_available: bool,
):
    book = BookModel(
        title=book_title,
        category=category,
        stars=stars,
        price=price,
        is_available=is_available,
    )
    insert_db(book)
    console.print(f"book: {book_title} inserted", style="info")
    return


@app.command()
def select_title(title: str):
    query = select_db_by_name(title)
    if query:
        __add_rows(query, book_table)
        console.print(book_table)
        return
    console.print(f"title: {title} not found", style="warning")
    return


@app.command()
def rows():
    console.print(f"{num_rows()} Rows.", style="info")
