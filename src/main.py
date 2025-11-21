# seattle/helpers/
import asyncio
import pandas as pd
import sqlite3

from src.helpers.httpx_asyncronous import fetch_data


async def main():
    urls = [f"https://quotes.toscrape.com/page/{i}/" for i in range(1, 11)]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    box = []
    for x in results:
        box = box + x
    return box


if __name__ == "__main__":
    list = asyncio.run(main())
    df = pd.DataFrame(list)
    df.to_csv("results_async.csv", index=False)

    conn = sqlite3.connect("results.db")
    df.to_sql("quotes", conn, if_exists="replace", index=True)
    conn.commit()
    df1 = pd.read_sql_query("SELECT * FROM quotes;", conn)
    print(df1.info())
    conn.close()
