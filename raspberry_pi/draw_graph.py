import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime

#laptop
save_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\graphs"
read_dir = r"C:\Users\shun\Documents\programming\WeatherData_Logger\raspberry_pi\csv\\"
#raspi
#save_dir =
date = datetime.datetime.today()
filename = date.strftime("%Y%m%d")
read_file = read_dir + filename + '.csv'

data = pd.read_csv(read_file, index_col='time')
df_tmp_humid = data.iloc[:, [0, 2]]
df_tmp_humid.plot()
plt.savefig(os.path.join(save_dir, "tmp_humid.png"))
plt.show()