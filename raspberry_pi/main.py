import bme280_csv as bme
import loggercsv as log

weather_data = bme.readData()
log.loggercsv(weather_data)