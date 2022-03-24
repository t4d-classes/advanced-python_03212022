""" params query """

import pyodbc

from db_demos.connection_info import conn_string


def run() -> None:
    """ run """

    with pyodbc.connect(conn_string) as conn:

        with conn.cursor() as cur:

            cur.execute("select * from rates where ratesid = 4")

            rate = cur.fetchone()

            if rate:
                print("record exists")
                print(rate)


if __name__ == "__main__":
    run()