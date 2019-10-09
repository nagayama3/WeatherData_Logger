import loggercsv as log

weather_data = bme.readData()
log.loggercsv(weather_data)