""" get rates """

from datetime import date

import requests

from rates_demo.business_days import business_days

def get_rates(start_date: date, end_date: date) -> list[str]:
    """ get rates """

    rate_responses: list[str] = []

    currency_symbols = ['USD', 'CAD', 'GBP']

    for business_day in business_days(start_date, end_date):

        rate_url = "".join([
            "http://127.0.0.1:5000/api/",
            str(business_day),
            "?base=INR&symbols=",
            ",".join(currency_symbols)
        ])

        response = requests.get(rate_url)
        rate_responses.append(response.text)

    return rate_responses
