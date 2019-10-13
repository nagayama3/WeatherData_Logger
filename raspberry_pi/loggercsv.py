import pandas as pd
import numpy as np
import datetime
import time
import csv
import os
import bme280_csv as bme

date = datetime.datetime.today()
csv_dir = os.path.dirname(os.path.abspath(__file__)) + '/csv'
filename = date.strftime("%Y-%m-%d")
filepath = csv_dir + '/' + filename + '.csv'

def create_csv():
    print(filepath)
    f = open(filepath, 'w')
    f.close()

def make_header():
    df = pd.DataFrame([], columns=['time', 'temp', 'press', 'hum'])
    df.to_csv(filepath, mode='a', index=False)

def writein_csv(weather_data):
    df = pd.DataFrame(weather_data)
    print(filepath)
    df.to_csv(filepath, mode = 'a', header=False, index=False)
    df = pd.read_csv(filepath, index_col=0)

if __name__ == "__main__":
    try:
        if os.path.isfile(filepath) == False:
            create_csv()
            make_header()
        weather_data = bme.readData()
        #weather_data = [[13, 28.0, 1000.0, 56]]
        print(weather_data)
        writein_csv([weather_data])
    except:
        pass
