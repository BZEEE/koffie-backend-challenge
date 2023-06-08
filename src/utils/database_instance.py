import sqlite3
import pandas as pd
from enum import Enum


class FetchOptions(Enum):
    FETCH_ONE = 1
    FETCH_MANY = 2
    FETCH_ALL = 2


class DatabaseInstance:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def execute_query(self, query: str, fetch_option: FetchOptions, is_commit: bool):
        query = self.cursor.execute(query)
        if is_commit:
            self.connection.commit()
            return
        if fetch_option == FetchOptions.FETCH_ONE:
            return query.fetchone()
        elif fetch_option == FetchOptions.FETCH_MANY:
            return query.fetchmany()
        elif fetch_option == FetchOptions.FETCH_ALL:
            return query.fetchall()

    def export_database_parquet_format(self, filename):
        data_frames = []
        get_all_tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
        for table in self.execute_query(get_all_tables_query, FetchOptions.FETCH_ALL, False):
            table_name = table[0]
            data_frames.append(pd.read_sql('SELECT * from ' + table_name, self.connection))
        merged_frames = pd.concat(data_frames)
        merged_frames.to_parquet(filename, index=False)
