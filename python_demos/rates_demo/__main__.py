""" rates demo main """

from datetime import date, timedelta

from rates_demo.get_rates import get_rates


if __name__ == "__main__":

    start_date = date(2021, 1, 1)
    end_date = start_date + timedelta(days=19)

    rates = get_rates(start_date, end_date)

    print("\n".join(rates))
