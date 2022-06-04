import pandas as pd
import sqlite3
import fetch


def read_tsv_file(file_path):
    '''
    :param file_path:  TSV path
    :return: Return DataFrame
    '''

    df = pd.read_csv(file_path, delimiter='\t')

    df.columns=['range_start',
                    'range_end',
                    'as_number',
                    'as_country_code',
                    'as_description']
    return df


def connect_database(db_file_path, DataFrame):

    '''
    :param db_file_path:  Path for the SQlite Database
    :param DataFrame: Dataframe from read_tsv_file
    :return: None
    '''

    connection= sqlite3.connect(db_file_path)
    DataFrame.to_sql(name = 'as_table',
                    con = connection,
                    if_exists='replace',
                    index=False,
                    dtype={ "range_start": "real",
                            "range_end": "real",
                            "as_number":"real",
                            "as_country_code":"text",
                            "as_description":"text" })
    return connection

def to_view(connection):
    cur = connection.cursor()
    cur.execute("SELECT * FROM as_table")
    rows = cur.fetchall()
    return rows

def get_as_from_as_number(connection,number):
    '''

    :param connection:
    :param number: As_number
    :return: rows of the specific as_numberer
    '''
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM as_table where as_number={number}")
    rows = cur.fetchall()

    rows = [dict(zip(["range_start","range_end","as_number","as_country_code",
                      "as_description"],row)) for row in rows]
    print('sample:', rows[:1])
    return rows

def get_as_from_ip_range(connection,ip_range_start):

    '''

    :param connection:
    :param number: ip_range_start
    :return: rows of the specific as_numberer
    '''
    cur=connection.cursor()
    cur.execute(f'SELECT * FROM as_table where range_start="{ip_range_start}"')
    rows= cur.fetchall()
    rows = [dict(zip(["range_start","range_end","as_number","as_country_code",
                      "as_description"],row)) for row in rows]
    print('sample',rows[:1])
    return rows
