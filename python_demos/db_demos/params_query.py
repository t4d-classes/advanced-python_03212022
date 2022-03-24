""" params query """

import pyodbc

from db_demos.connection_info import conn_string


def run() -> None:
    """ run """

    with pyodbc.connect(conn_string) as conn:

        currency_symbol = input("Please enter a currency symbol > ")

        rates = conn.execute(
            "select * from rates where currencysymbol = ?", (currency_symbol, ))

        for rate_row in rates:
            print(rate_row)


if __name__ == "__main__":
    run()