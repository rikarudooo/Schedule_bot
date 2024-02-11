import requests
import csv

from flask import Flask
from datetime import datetime

app = Flask(__name__)

token =
chat_id =

# Endpoint untuk waktu sekarang
@app.route('/schedule', methods=['GET'])
def get_schedule():
    # read from cvs
    data = read_csv("source.csv")

    # Membuat datetime
    day = int(data[0][0])
    month = int(data[0][1])
    year = int(data[0][2])
    specific_date = datetime(year, month, day)

    now = datetime.now()
    if datetime(now.year, now.month, now.day) == specific_date:
        tanggal = data[0][0] + "-" + data[0][1] + "-" + data[0][2]
        message = f"hari ini tanggal {tanggal} ada meeting"
        send_message(token, chat_id, message)
    return ""

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        # Skip header row
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=params)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Error: {response.status_code} - {response.text}")


if __name__ == '__main__':
    app.run(debug=True)
