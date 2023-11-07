import json
import sqlite3
import certifi
import pandas as pd
import urllib3


def import_data():
    df_csv = pd.read_csv("")
    df_parquet = pd.read_parquet("yellow_tripdata_2022-01")