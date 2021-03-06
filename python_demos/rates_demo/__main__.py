""" rates demo main """

from datetime import date, timedelta

from rates_demo.rates_api_server import rates_api_server
from rates_demo.get_rates import get_rates_threaded


if __name__ == "__main__":

    print("start app")

    with rates_api_server():

        print("start get rates")
        start_date = date(2021, 1, 1)
        end_date = start_date + timedelta(days=19)
        currency_symbols = ['USD', 'CAD', 'GBP']

        rates = get_rates_threaded(
            start_date, end_date, "INR", currency_symbols)

        print("\n".join(rates))
        print(rates)
        print(len(rates))
        print("end get rates")

    print("end app")
