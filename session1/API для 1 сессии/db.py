import pyodbc


def get_connection():
    SERVER = 'POLNAREFF\\SQLEXPRESS'
    DATABASE = 'SAM'
    conn_str = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes;"
    )

    conn = pyodbc.connect(conn_str)
    return conn