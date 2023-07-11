def casting_stars_num(string_num: str) -> int:
    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    if string_num in nums:
        return nums[string_num]
    raise ValueError("stars number isn't valid.")

def casting_stock(string: str) -> bool:
    if string == "In stock":
        return True
    return False