from book_club.core.crud import insert_db, create_db, select_db, num_rows
from book_club.scraping.scraping import get_url_by_category, get_book
from book_club.models.book_model import BookModel
import typer
from rich.table import Table, Row
from rich.console import Console

app = typer.Typer()


@app.command()
def create():
    create_db()
    return


@app.command()
def load():
    for category, url in get_url_by_category():
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

    print(type(ids))

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
        case 1:
            __add_rows(select_db(ids[0]), book_table)
            console.print(book_table)
            return
        case _ if len(ids) > 1:
            for book in select_db(ids):
                print(type(book))
                __add_rows(book, book_table)
            console.print(book_table)
            return
        case _:
            console.print("Find another method.")
            return


@app.command()
def rows():
    print(f"{num_rows()} Rows.")


if __name__ == "__main__":
    app()
