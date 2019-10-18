#coding: utf-8
import requests
import argparse
import datetime

save_dir = r"/home/pi/Documents/WeatherData_Logger/raspberry_pi/graphs/"
filename = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(1), "%Y-%m-%d")
pic_path = save_dir + filename + ".png"

def main(*args):
    url = "https://notify-api.line.me/api/notify"
    token = "jElh7raXhrBrHKAUomKPX9C07UzH54yoYEqeaK1C2yE"
    headers = {"Authorization" : "Bearer" + token}

    message = filename + "の我が家の気象データ"
    payload = {"message" : message}
    
    if len(args) == 0:
        pass
    else:
        files = {"imageFile" : open(save_dir + filename + ".png", "rb")}
        requests.post(url, data=payload, headers=headers, files=files)

if __name__ == "__main__":
    main(pic_path)