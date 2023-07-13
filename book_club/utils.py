from pathlib import Path
from book_club.core.config import settings
from book_club.models.book_model import BookModel


def casting_stars_num(string_num: str) -> int:
    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    if string_num in nums:
        return nums[string_num]
    raise ValueError("stars number isn't valid.")


def casting_stock(string: str) -> bool:
    if string == "In stock":
        return True
    return False


def to_csv(models: list[BookModel], path: str):
    file_path = Path(path)
    header = "title,stars,price,is_available,category"
    if file_path.exists():
        with open(file_path / "book_club.csv", "a+", encoding="utf-8") as file:
            file.seek(0)
            if file.readlines().__len__() == 0:
                file.write(header + "\n")
            for model in models:
                file.write(
                    f"{model.title},{model.stars},{model.price},"
                    f"{model.is_available},{model.category}"
                )
        return
    raise Exception("Path not found.")
