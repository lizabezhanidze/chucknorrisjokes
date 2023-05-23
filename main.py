import requests
from win10toast import ToastNotifier
import json
import sqlite3
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
print("statuscode", response.status_code)
print("headers", response.headers)
data = response.json()
joke = data["value"]
print(joke)
with open("jokes.json", "w") as f:
    f.write(json.dumps(data))

conn = sqlite3.connect("chuck.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS jokes (
	id integer PRIMARY KEY,
	joke text NOT NULL);""")
cursor.execute(f"INSERT INTO jokes (joke)VALUES ('{joke}')")
ToastNotifier().show_toast("Joke", joke)


