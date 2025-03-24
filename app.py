import pandas as pd
import os
from dotenv import load_dotenv


def read_csv(file):
    df_reader = pd.read_csv(file, chunksize=10000)
    return df_reader


def transform_data(df):
    df["duration_fullmin"] = df["duration_ms"] // (1000 * 60)
    df["track_year"] = df["track_album_release_date"].str[:4]
    df["track_yearmonth"] = df["track_album_release_date"].str[:7]
    return df


def to_sql(df, db_conn_uri, ds_name):
    df.to_sql(
        ds_name,
        db_conn_uri,
        if_exists='append',
        index=False
    )


def db_loader(file, db_conn_uri, ds_name):
    df_reader = read_csv(file)
    for idx, df in enumerate(df_reader):
        df_transformed = transform_data(df)
        print(f'Populating chunk {idx} of {ds_name}')
        to_sql(df_transformed, db_conn_uri, ds_name)


def process_files():
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_conn_uri = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

    SONGS_DATA = "data/spotify_songs.csv"

    db_loader(SONGS_DATA, db_conn_uri, "song")


if __name__ == '__main__':
    load_dotenv()
    process_files()