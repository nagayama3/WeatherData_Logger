#coding: utf-8
import requests
import argparse
import datetime
import sys

filename = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")
read_file = read_dir + filename + '.csv'

def main():
    url = "https://notify-api.line.me/api/notify"
    token = "HuJBwmzKyIVh2MX8WJtHu9mmb4Ap3j53WEzXcpiDL68"
    headers = {"Authorization" : "Bearer" + token}

    message = filename + "の我が家の気象データ"
    payload = {"message" : message}
    files = {"imageFile" : open(save_dir + read_file, "rb")}

    line_notify = requests.post(url, data=payload, headers=headers, files=file)

if __name__ == "__main__":
    main()