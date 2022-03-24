""" params query """

import pyodbc

from db_demos.connection_info import conn_string


def run() -> None:
    """ run """

    with pyodbc.connect(conn_string) as conn:

        with conn.cursor() as cur:

            params = [
                ("2021-10-03", "INR", 80),
                ("2021-10-03", "USD", 1.10),
                ("2021-10-03", "GBP", 0.90),
                ("2021-10-03", "CAD", 1.40),
                ("2021-10-03", "BTC", 33000)
            ]

            cur.executemany(
                "insert into rates (closingdate, currencysymbol, exchangerate)"
                "values (?, ?, ?)",
                params)


if __name__ == "__main__":
    run()