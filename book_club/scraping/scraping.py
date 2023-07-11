from bs4 import BeautifulSoup
from book_club.scraping.request import book_request
from book_club.utils import casting_stars_num, casting_stock
from book_club.models.book_model import BookModel
from book_club.core.config import settings


def get_url_by_category() -> list:
    base_response = book_request(settings.BOOK_BASE_URL)

    base_response_parser = BeautifulSoup(base_response, "html.parser")

    categories = base_response_parser.find("div", class_="side_categories")
    return [
        (
            category.text.strip(),
            settings.BOOK_BASE_URL + category.a.get("href"),
        )
        for category in categories.find_all("li")[1:]
    ]


def get_book(url: str, category: str) -> list[dict[str, str | float]]:
    books = []
    book_response = book_request(url)

    book_parser = BeautifulSoup(book_response, "html.parser")

    articles = book_parser.find_all("article", class_="product_pod")

    # book_name, category, stars, price, is_available

    for article in articles:
        books.append(
            BookModel(
                title=article.h3.a.get("title"),
                stars=casting_stars_num(article.p.get("class")[1].lower()),
                price=float(
                    article.find("p", class_="price_color").text.replace(
                        "Â£", ""
                    )
                ),
                is_available=casting_stock(
                    article.find(
                        "p", class_="instock availability"
                    ).text.strip()
                ),
                category=category,
            )
        )

    next_pagination = book_parser.find("ul", class_="pager")
    if next_pagination:
        if next_pagination.a.text == "next":
            books += get_book(
                url.replace("index.html", next_pagination.a.get("href")),
                category,
            )
            return books
    return books
