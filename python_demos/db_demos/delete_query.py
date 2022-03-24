""" params query """

import pyodbc

from db_demos.connection_info import conn_string


def run() -> None:
    """ run """

    with pyodbc.connect(conn_string) as conn:

        conn.execute(
            "delete from rates where ratesid = ?",
            (3,))


if __name__ == "__main__":
    run()