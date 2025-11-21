import httpx
from bs4 import BeautifulSoup as bs
from loguru import logger



async def fetch_user(url_: str) -> str:
    logger.info("entered fetch_user")
    with httpx.Client() as client:
        response = client.get(url_)
        return response.text


# try async


async def fetch_user_async(url_: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url_)
        response.raise_for_status()
        return response.text


# **********************************************************
def parse_page(soup: bs) -> list:
    quote_box = soup.select_one("div", class_="row").select("div.quote")

    res_ = []
    for q in quote_box:
        quote_ = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        res = {"quote": quote_, "author": author}
        res_.append(res)

    return res_


async def fetch_data(url_):
    logger.info("entered fetch_data()")
    async with httpx.AsyncClient() as client:
        response_ = await client.get(url_)
        soup = bs(response_.text, "html.parser")
        list_ = parse_page(soup)
        return list_
