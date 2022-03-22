""" get rates """

from concurrent.futures import ThreadPoolExecutor
import threading

from datetime import date

import requests

from rates_demo.business_days import business_days

def get_rates(start_date: date, end_date: date) -> list[str]:
    """ get rates """

    rate_responses: list[str] = []

    currency_symbols = ['USD', 'CAD', 'GBP']

    for business_day in business_days(start_date, end_date):

        rate_url = "".join([
            "http://127.0.0.1:5050/api/",
            str(business_day),
            "?base=INR&symbols=",
            ",".join(currency_symbols)
        ])

        response = requests.get(rate_url)
        print(response.status_code)
        rate_responses.append(response.text)

    return rate_responses

def get_rate_task(business_day: date) -> str:
    """ get rate task """

    currency_symbols = ['USD', 'CAD', 'GBP']

    rate_url = "".join([
        "http://127.0.0.1:5050/api/",
        str(business_day),
        "?base=INR&symbols=",
        ",".join(currency_symbols)
    ])

    response = requests.get(rate_url)
    return str(response.status_code)


def get_rates_threadpool(start_date: date, end_date: date) -> list[str]:
    """ get rates threaded """

    rate_responses: list[str] = []

    with ThreadPoolExecutor(max_workers=12) as executor:
        rate_responses = list(executor.map(
            get_rate_task,
            [ business_day
              for business_day in business_days(start_date, end_date) ]
        ))

    return rate_responses


def get_rate_task2(
    business_day: date, base_currency: str,
    currency_symbols: list[str], responses: list[str]) -> None:
    """ get rate task2 """

    rate_url = "".join([
        "http://127.0.0.1:5050/api/",
        str(business_day),
        "?base=" + base_currency + "&symbols=",
        ",".join(currency_symbols)
    ])

    response = requests.get(rate_url)
    responses.append(response.text)


def get_rates_threaded(
    start_date: date, end_date: date,
    base_currency: str, currency_symbols: list[str]) -> list[str]:
    """ get rates """

    rate_responses: list[str] = []
    threads: list[threading.Thread] = []

    for business_day in business_days(start_date, end_date):
        a_thread = threading.Thread(
            target=get_rate_task2,
            args=(business_day,base_currency,currency_symbols,rate_responses))
        a_thread.start()
        threads.append(a_thread)

    for a_thread in threads:
        a_thread.join()

    return rate_responses
