import pandas as pd
import numpy as np
import datetime
import time
import csv
import os
#import bme280_csv as bme

date = datetime.datetime.today()
time = datetime.datetime.now()
csv_dir = os.path.dirname(os.path.abspath(__file__)) + '\csv'
filename = 'sample2'
filepath = csv_dir + '/' + filename + '.csv'

def create_csv():
    # print(filepath)
    f = open(filepath, 'w')
    f.close()

def make_header():
    df = pd.DataFrame([], columns=['time', 'temp', 'press', 'hum'])
    df.to_csv(filepath, mode='a', index=False)

def writein_csv(weather_data):
    df = pd.DataFrame(weather_data)
    df.to_csv(filepath, mode = 'a', header=False, index=False)
    df = pd.read_csv(filepath, index_col=0)
    print(df)


if __name__ == "__main__":
    try:
        if os.path.isfile(filepath) == False:
            create_csv()
            make_header()
        #weather_data = bme.readData()
        temp = 20.0
        press = 1000.0
        hum = 10
        for i in range(24):
            time_ = time.strftime("%Y-%m-%d %H:%M")
            weather_data = [[time_, temp, press, hum]]
            writein_csv(weather_data)
            temp += i*1
            press += i
            hum += i / 10
            #time.sleep(0.01)
            
    except:
        pass