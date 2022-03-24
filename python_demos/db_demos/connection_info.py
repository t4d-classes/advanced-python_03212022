# local_conn_options = [
#     "DRIVER={ODBC Driver 17 for SQL Server}",
#     "SERVER=localhost\SQLExpress",
#     "DATABASE=ratesapp",
#     "UID=sa",
#     "PWD=sqlDbp@ss!",
# ]

docker_conn_options = [
    "DRIVER={ODBC Driver 17 for SQL Server}",
    "SERVER=localhost,1433",
    "DATABASE=ratesapp",
    "UID=sa",
    "PWD=sqlDbp@ss!",
]

# azure_conn_options = [
#     "DRIVER={ODBC Driver 17 for SQL Server}",
#     "SERVER=advpython03212022.database.windows.net",
#     "DATABASE=rates_app",
#     "UID=advpython03212022user",
#     "PWD=sqlDbp@ss!",
# ]

conn_string = ";".join(docker_conn_options)