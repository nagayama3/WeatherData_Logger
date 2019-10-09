import pandas as pd
import numpy as np
import datetime
import csv
import os

date = datetime.datetime.today()
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = date.strftime("%Y%m%d")

filepath = current_dir + '/' + filename + '.csv'

def writein_csv():
    df = pd.DataFrame([[0,1,2], [3,4,5], [6,7,8]])
    df.to_csv(filepath)
    print(df)

def create_csv():
    # print(filepath)
    if os.path.isfile(filepath) == False:
        f = open(filepath, 'w')
        df = pd.read_csv(filepath)
        f.close()
    df = pd.DataFrame(['time', 'temp', 'press', 'hum'])
    df.to_csv(filepath)
    print(df)

if __name__ == "__main__":
    try:
        create_csv()
        writein_csv()
    except:
        pass