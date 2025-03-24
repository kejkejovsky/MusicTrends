import matplotlib.pyplot as plt
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_conn_uri = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

df = pd.read_sql("SELECT * FROM song;", db_conn_uri)
df_grouped = df.groupby("track_year")["duration_fullmin"].mean().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(df_grouped["track_year"], df_grouped["duration_fullmin"], marker="o", linestyle="-")
plt.xlabel("Rok")
plt.ylabel("Średnia długość piosenek (min)")
plt.title("Zmiana długości piosenek na przestrzeni lat")
plt.grid()
plt.show()
