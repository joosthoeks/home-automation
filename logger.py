#!/usr/bin/env python3


# Import Built-Ins:
import configparser
from datetime import datetime as dt
import os
import time

# Import Third-Party:
from influxdb_client import InfluxDBClient, Point
from influxdb_client .client.write_api import SYNCHRONOUS

# Import Homebrew:
from sensors import Sensors


class Logger:

    def __init__(self):
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_file)
        self.client = InfluxDBClient.from_config_file(config_file)
        self.bucket = config['ha']['influx_bucket']
        self.sensors = Sensors()

    def append_row(self, sensor_name, value):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        point = Point('sensor').field(sensor_name, value)
        write_api.write(bucket=self.bucket, record=point)

    def run(self):

        while True:

            dummy0 = self.sensors.get_dummy_sensor0()
            self.append_row('dummy0', dummy0)
            
            dummy1 = self.sensors.get_dummy_sensor1()
            self.append_row('dummy1', dummy1)

            temperature_outside = self.sensors.get_temperature_outside()
            self.append_row('temperature_outside', temperature_outside)
            
            humidity_outside = self.sensors.get_humidity_outside()
            self.append_row('humidity_outside', humidity_outside)
            
            pressure_outside = self.sensors.get_pressure_outside()
            self.append_row('pressure_outside', pressure_outside)
            
            light_outside = self.sensors.get_light_outside()
            self.append_row('light_outside', light_outside)
            
            decibel_outside = self.sensors.get_decibel_outside()
            self.append_row('decibel_outside', decibel_outside)
            
            temperature_pool_outside = self.sensors.get_temperature_pool_outside()
            self.append_row('temperature_pool_outside', temperature_pool_outside)
            
            wind = self.sensors.get_wind()
            self.append_row('wind', wind)
            
            doorbell = self.sensors.get_doorbell()
            self.append_row('doorbell', doorbell)
            
            temperature1 = self.sensors.get_temperature1()
            self.append_row('temperature1', temperature1)
            
            humidity1 = self.sensors.get_humidity1()
            self.append_row('humidity1', humidity1)
            
            pressure1 = self.sensors.get_pressure1()
            self.append_row('pressure1', pressure1)
            
            light1 = self.sensors.get_light1()
            self.append_row('light1', light1)
            
            decibel1 = self.sensors.get_decibel1()
            self.append_row('decibel1', decibel1)
            
            pir1 = self.sensors.get_pir1()
            self.append_row('pir1', pir1)
            
            ultrasonic1 = self.sensors.get_ultrasonic1()
            self.append_row('ultrasonic1', ultrasonic1)
            
            temperature2 = self.sensors.get_temperature2()
            self.append_row('temperature2', temperature2)
            
            humidity2 = self.sensors.get_humidity2()
            self.append_row('humidity2', humidity2)
            
            pressure2 = self.sensors.get_pressure2()
            self.append_row('pressure2', pressure2)
            
            light2 = self.sensors.get_light2()
            self.append_row('light2', light2)
            
            decibel2 = self.sensors.get_decibel2()
            self.append_row('decibel2', decibel2)
            
            pir2 = self.sensors.get_pir2()
            self.append_row('pir2', pir2)
            
            ultrasonic2 = self.sensors.get_ultrasonic2()
            self.append_row('ultrasonic2', ultrasonic2)
            
            temperature3 = self.sensors.get_temperature3()
            self.append_row('temperature3', temperature3)
            
            humidity3 = self.sensors.get_humidity3()
            self.append_row('humidity3', humidity3)
            
            pressure3 = self.sensors.get_pressure3()
            self.append_row('pressure3', pressure3)
            
            light3 = self.sensors.get_light3()
            self.append_row('light3', light3)
            
            decibel3 = self.sensors.get_decibel3()
            self.append_row('decibel3', decibel3)
            
            pir3 = self.sensors.get_pir3()
            self.append_row('pir3', pir3)
            
            ultrasonic3 = self.sensors.get_ultrasonic3()
            self.append_row('ultrasonic3', ultrasonic3)
            
            temperature4 = self.sensors.get_temperature4()
            self.append_row('temperature4', temperature4)
            
            humidity4 = self.sensors.get_humidity4()
            self.append_row('humidity4', humidity4)
            
            pressure4 = self.sensors.get_pressure4()
            self.append_row('pressure4', pressure4)
            
            light4 = self.sensors.get_light4()
            self.append_row('light4', light4)
            
            decibel4 = self.sensors.get_decibel4()
            self.append_row('decibel4', decibel4)
            
            pir4 = self.sensors.get_pir4()
            self.append_row('pir4', pir4)
            
            ultrasonic4 = self.sensors.get_ultrasonic4()
            self.append_row('ultrasonic4', ultrasonic4)
            
            temperature5 = self.sensors.get_temperature5()
            self.append_row('temperature5', temperature5)
            
            humidity5 = self.sensors.get_humidity5()
            self.append_row('humidity5', humidity5)
            
            pressure5 = self.sensors.get_pressure5()
            self.append_row('pressure5', pressure5)
            
            light5 = self.sensors.get_light5()
            self.append_row('light5', light5)
            
            decibel5 = self.sensors.get_decibel5()
            self.append_row('decibel5', decibel5)
            
            pir5 = self.sensors.get_pir5()
            self.append_row('pir5', pir5)
            
            ultrasonic5 = self.sensors.get_ultrasonic5()
            self.append_row('ultrasonic5', ultrasonic5)
            
            temperature_pool_inside = self.sensors.get_temperature_pool_inside()
            self.append_row('temperature_pool_inside', temperature_pool_inside)
            

logger = Logger()
logger.run()
