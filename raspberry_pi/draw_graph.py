import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

#laptop
save_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\graphs"
read_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\csv\\"
#raspi
#save_dir =
date = datetime.today()
filename = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")
read_file = read_dir + filename + '.csv'

data = pd.read_csv(read_file, index_col='time')
title = date.strftime('%Y%m%d') + '@myhome'
pic_name = date.strftime('%Y%m%d') + '.png'

#temperature
fig, ax_1 = plt.subplots()
ax_2 = ax_1.twinx()
df = data.iloc[:, [0, 2]]
ax_1.plot(df)
ax_1.set_title(title)
ax_1.set_ylabel('temperature, humdity')

df = data.iloc[:, [1]]
ax_2.plot(df, color='green')
ax_2.set_ylabel('pressure')

labels = ax_1.get_xticklabels()
plt.setp(labels, rotation=70)
plt.show()
plt.savefig(os.path.join(save_dir, pic_name))