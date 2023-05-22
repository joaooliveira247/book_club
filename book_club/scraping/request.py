from requests import get, Response, HTTPError

def book_request(url: str) -> str:
    response: Response = get(url)
    if response.status_code != 200:
        raise HTTPError(
            f"{url} returns {response.status_code} code, try again later."
            )
    return response.text