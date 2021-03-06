""" Test Utils Module """

from unittest import TestCase, main
from unittest.mock import patch, mock_open
import pathlib


from rates_shared.rates_shared import parse_command, read_config

# mock data
YAML_CONFIG = """server:
  host: 127.0.0.1
  port: 5050
database:
  server: 127.0.0.1,1433
  database: ratesapp
  username: sa
  password: sqlDbp@ss!"""


class TestRatesShared(TestCase):
    """ test rates shared class"""

    def test_parse_command_junk(self) -> None:
        """ test parse command """

        # Arrange
        client_command = "JUNK"

        # Act
        result = parse_command(client_command)

        # Assert
        self.assertEqual(result, None)

    def test_parse_command(self) -> None:
        """ test parse command """

        client_command = "GET 2021-04-01 CAD"

        result = parse_command(client_command)

        self.assertEqual(result, {
            "name": "GET",
            "date": "2021-04-01",
            "symbols": "CAD"
        })

    def test_read_config(self) -> None:
        """ test read config """

        with patch('rates_shared.rates_shared.open',
                   mock_open(read_data=YAML_CONFIG)) as mock:

            config = read_config()

            self.assertEqual(config, {
                "server": {
                    "host": "127.0.0.1",
                    "port": 5050,
                },
                "database": {
                    "server": "127.0.0.1,1433",
                    "database": "ratesapp",
                    "username": "sa",
                    "password": "sqlDbp@ss!"
                }})

            mock.assert_called_once_with(
                pathlib.Path("config", "rates_config.yaml")
            )
