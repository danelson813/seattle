import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    results = []
    for i in range(1, 11):
        url = f"https://quotes.toscrape.com/page/{i}/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        quotes = soup.select_one("div", class_="row").select("div.quote")

        for q in quotes:
            result = {
                "quote": q.find("span", class_="text").text.replace('"“', '"'),
                "author": q.find("small", class_="author").text,
            }
            results.append(result)

    df = pd.DataFrame(results)
    df.to_csv("data/results.csv", index=False)


if __name__ == "__main__":
    main()
