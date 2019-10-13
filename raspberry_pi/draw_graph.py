import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

#laptop
#save_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\graphs"
#read_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\csv\\"

#raspi
save_dir = r"/home/pi/Documents/WeatherData_Logger/raspberry_pi/graphs"
read_dir = r"/home/pi/Documents/WeatherData_Logger/raspberry_pi/csv/"

date = datetime.today()
filename = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")
read_file = read_dir + filename + '.csv'

data = pd.read_csv(read_file, index_col='time')
title = date.strftime('%Y%m%d') + '@myhome'
pic_name = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d') + '.png'

#GRAPH
fig, ax = plt.subplots()
#temperature
df = data.iloc[:, [0]]
l1, = ax.plot(df, color='r', label='temp')

#xaxis
#ax.xaxis.set_major_locator(mdates.HourLocator(byhour=(range(0, 24, 3))))
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

ax.set_title(title)
ax.set_ylabel('temperature(℃)')
#ax.legend(loc="lower left")
plt.ylim(0, 40)

#pressure
df = data.iloc[:, [1]]
ax_2 = ax.twinx()
l2, = ax_2.plot(df, color='g', label='press')
ax_2.set_ylabel('pressure(hPa)')
#ax_2.legend(loc="lower left")

#humdity
df = data.iloc[:, [2]]
ax_3 = ax.twinx()
l3, = ax_3.plot(df, color='b', label='hum')
ax_3.set_ylabel('humdity(%)')
rspine = ax_2.spines['right']
rspine.set_position(('axes', 1.25))
plt.ylim(0, 100)
#ax_3.legend(loc="lower left")

fig.subplots_adjust(right=0.75)

labels = ax.get_xticklabels()
plt.setp(labels, rotation=70)
plt.legend([l1, l2, l3], ["temp", "press", "hum"])
plt.show()

plt.show()
plt.savefig(os.path.join(save_dir, pic_name))
