import pandas as pd
import matplotlib.pyplot as plt
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
fig, ax1 = plt.subplots()
df = data.iloc[:, [0, 2]]
ax1.plot(df)

ax2 = ax1.twinx()
df = data.iloc[:, [1]]
ax2.plot(df)
plt.show()