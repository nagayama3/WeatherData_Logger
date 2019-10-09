import pandas as pd
import datetime
import csv
import os

date = datetime.datetime.today()
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = date.strftime("%Y%m%d")

filepath = current_dir + '/' + filename + '.csv'

def writein_csv():
    df = pd.read_csv(filepath, names = [hour, minute, temp, press, hum])
    


if __name__ == "__main__":
    try:
        writein_csv()
    except:
        pass