""" dates demo """

from datetime import datetime, timedelta, date
import time

def run_demo() -> None:
    """ run demo """

    start_time = time.time()

    print(start_time)

    start = datetime.now()
    end = start + timedelta(days=180)

    print(start)
    print(end)

    print(type(start))
    print(type(timedelta(days=180)))

    independence_day = date(1776, 7, 4)

    print(independence_day)
    print(type(independence_day))

    print(datetime.now().strftime("%B %A"))

    tax_day_str = "04-2022-18"

    tax_day = datetime.strptime(tax_day_str, "%m-%Y-%d")

    print(tax_day)
    print(type(tax_day))

    end_time = time.time()

    print(end_time - start_time)

    print(datetime.now().weekday())
    # monday -> 0
    # tuesday -> 1
    # etc...


