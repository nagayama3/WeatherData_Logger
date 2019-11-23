#coding: utf-8
import requests
import argparse
import datetime
import sys

save_dir = r"/home/pi/Documents/WeatherData_Logger/raspberry_pi/graphs/"
filename = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(1), "%Y-%m-%d")
pic_path = save_dir + filename + ".png"

url = "https://notify-api.line.me/api/notify"
token = "aqQGPAfipAeWts6MY0vvh4cnZpSSjsmW7s3vaWC5IAB"
headers = {"Authorization" : "Bearer" + token}

message = filename
payload = {"message" : message}
#print(message)
#print(pic_path)
#files = {"imageFile" : open(pic_path, "rb")}
r = requests.post(url, headers=headers, data=payload)
print(r)
