""" Main Test Module """

from unittest import TestSuite, TextTestRunner

from tests.test_sample import TestSample
from tests.tests_rates_shared import TestRatesShared


def suite() -> TestSuite:
    """ Create Test Suite for Main Test Module """

    test_suite = TestSuite()
    test_suite.addTest(TestSample())
    test_suite.addTest(TestRatesShared())
    return test_suite


if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(suite())
