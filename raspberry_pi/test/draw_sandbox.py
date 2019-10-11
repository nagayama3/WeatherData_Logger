import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import datetime

date = datetime.datetime.today()
#laptop
save_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\graphs"
read_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\csv\\"
#raspi
#save_dir =
read_file = read_dir + 'sample2.csv'

data = pd.read_csv(read_file, index_col='time')
#df = data.iloc[:, [0, 2]]
#df.plot()
#plt.savefig(os.path.join(save_dir, "tmp_humid.png"))
#plt.show()

#GRAPH

title = date.strftime('%Y%m%d') + '@myhome'

#temperature
fig, ax_1 = plt.subplots()
ax_2 = ax_1.twinx()
df = data.iloc[:, [0, 2]]
#ax_1.callbacks.connect()
ax_1.plot(df)
ax_1.set_title(title)
ax_1.set_ylabel('temperature, humdity')

df = data.iloc[:, [1]]
ax_2.plot(df, color='green')
ax_2.set_ylabel('pressure')

labels = ax_1.get_xticklabels()
plt.setp(labels, rotation=70)
plt.show()