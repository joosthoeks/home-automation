#!/usr/bin/env python3.7


# Import Built-Ins:
import configparser
from datetime import datetime as dt
import os
import sys
import time

# Import Third-Party:
from influxdb_client import InfluxDBClient

# Import Homebrew:
from sensors import Sensors


if sys.version_info < (3, 7, 0):
    sys.exit('Python 3.7.0 or higher is required. You are using Python {}.{}.{}.'.format(sys.version_info[0], sys.version_info[1], sys.version_info[2]))


class Logger:

    def __init__(self):
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_file)
        client = InfluxDBClient.from_config_file(config_file)
        self.write_api = client.write_api()
        self.bucket = config['ha']['influx_bucket']
        self.sensors = Sensors()

    def add_record(self, measurement, tag_key, tag_value, field_key, field_value):
        # https://v2.docs.influxdata.com/v2.0/reference/syntax/line-protocol/
        line = [
        '{},{}={} {}={} {}'
        .format(measurement, tag_key, tag_value, field_key, field_value, time.time_ns())
        ]
        self.write_api.write(bucket=self.bucket, record=line)

    def run(self):

        while True:

            dummy0 = self.sensors.get_dummy_sensor0()
            self.add_record('sensor', 'location', 'home', 'dummy0', dummy0)
            
            dummy1 = self.sensors.get_dummy_sensor1()
            self.add_record('sensor', 'location', 'home', 'dummy1', dummy1)

            temperature_outside = self.sensors.get_temperature_outside()
            self.add_record('sensor', 'location', 'home', 'temperature_outside', temperature_outside)
            
            humidity_outside = self.sensors.get_humidity_outside()
            self.add_record('sensor', 'location', 'home', 'humidity_outside', humidity_outside)
            
            pressure_outside = self.sensors.get_pressure_outside()
            self.add_record('sensor', 'location', 'home', 'pressure_outside', pressure_outside)
            
            light_outside = self.sensors.get_light_outside()
            self.add_record('sensor', 'location', 'home', 'light_outside', light_outside)
            
            decibel_outside = self.sensors.get_decibel_outside()
            self.add_record('sensor', 'location', 'home', 'decibel_outside', decibel_outside)
            
            temperature_pool_outside = self.sensors.get_temperature_pool_outside()
            self.add_record('sensor', 'location', 'home', 'temperature_pool_outside', temperature_pool_outside)
            
            wind = self.sensors.get_wind()
            self.add_record('sensor', 'location', 'home', 'wind', wind)
            
            doorbell = self.sensors.get_doorbell()
            self.add_record('sensor', 'location', 'home', 'doorbell', doorbell)
            
            temperature1 = self.sensors.get_temperature1()
            self.add_record('sensor', 'location', 'home', 'temperature1', temperature1)
            
            humidity1 = self.sensors.get_humidity1()
            self.add_record('sensor', 'location', 'home', 'humidity1', humidity1)
            
            pressure1 = self.sensors.get_pressure1()
            self.add_record('sensor', 'location', 'home', 'pressure1', pressure1)
            
            light1 = self.sensors.get_light1()
            self.add_record('sensor', 'location', 'home', 'light1', light1)
            
            decibel1 = self.sensors.get_decibel1()
            self.add_record('sensor', 'location', 'home', 'decibel1', decibel1)
            
            pir1 = self.sensors.get_pir1()
            self.add_record('sensor', 'location', 'home', 'pir1', pir1)
            
            ultrasonic1 = self.sensors.get_ultrasonic1()
            self.add_record('sensor', 'location', 'home', 'ultrasonic1', ultrasonic1)
            
            temperature2 = self.sensors.get_temperature2()
            self.add_record('sensor', 'location', 'home', 'temperature2', temperature2)
            
            humidity2 = self.sensors.get_humidity2()
            self.add_record('sensor', 'location', 'home', 'humidity2', humidity2)
            
            pressure2 = self.sensors.get_pressure2()
            self.add_record('sensor', 'location', 'home', 'pressure2', pressure2)
            
            light2 = self.sensors.get_light2()
            self.add_record('sensor', 'location', 'home', 'light2', light2)
            
            decibel2 = self.sensors.get_decibel2()
            self.add_record('sensor', 'location', 'home', 'decibel2', decibel2)
            
            pir2 = self.sensors.get_pir2()
            self.add_record('sensor', 'location', 'home', 'pir2', pir2)
            
            ultrasonic2 = self.sensors.get_ultrasonic2()
            self.add_record('sensor', 'location', 'home', 'ultrasonic2', ultrasonic2)
            
            temperature3 = self.sensors.get_temperature3()
            self.add_record('sensor', 'location', 'home', 'temperature3', temperature3)
            
            humidity3 = self.sensors.get_humidity3()
            self.add_record('sensor', 'location', 'home', 'humidity3', humidity3)
            
            pressure3 = self.sensors.get_pressure3()
            self.add_record('sensor', 'location', 'home', 'pressure3', pressure3)
            
            light3 = self.sensors.get_light3()
            self.add_record('sensor', 'location', 'home', 'light3', light3)
            
            decibel3 = self.sensors.get_decibel3()
            self.add_record('sensor', 'location', 'home', 'decibel3', decibel3)
            
            pir3 = self.sensors.get_pir3()
            self.add_record('sensor', 'location', 'home', 'pir3', pir3)
            
            ultrasonic3 = self.sensors.get_ultrasonic3()
            self.add_record('sensor', 'location', 'home', 'ultrasonic3', ultrasonic3)
            
            temperature4 = self.sensors.get_temperature4()
            self.add_record('sensor', 'location', 'home', 'temperature4', temperature4)
            
            humidity4 = self.sensors.get_humidity4()
            self.add_record('sensor', 'location', 'home', 'humidity4', humidity4)
            
            pressure4 = self.sensors.get_pressure4()
            self.add_record('sensor', 'location', 'home', 'pressure4', pressure4)
            
            light4 = self.sensors.get_light4()
            self.add_record('sensor', 'location', 'home', 'light4', light4)
            
            decibel4 = self.sensors.get_decibel4()
            self.add_record('sensor', 'location', 'home', 'decibel4', decibel4)
            
            pir4 = self.sensors.get_pir4()
            self.add_record('sensor', 'location', 'home', 'pir4', pir4)
            
            ultrasonic4 = self.sensors.get_ultrasonic4()
            self.add_record('sensor', 'location', 'home', 'ultrasonic4', ultrasonic4)
            
            temperature5 = self.sensors.get_temperature5()
            self.add_record('sensor', 'location', 'home', 'temperature5', temperature5)
            
            humidity5 = self.sensors.get_humidity5()
            self.add_record('sensor', 'location', 'home', 'humidity5', humidity5)
            
            pressure5 = self.sensors.get_pressure5()
            self.add_record('sensor', 'location', 'home', 'pressure5', pressure5)
            
            light5 = self.sensors.get_light5()
            self.add_record('sensor', 'location', 'home', 'light5', light5)
            
            decibel5 = self.sensors.get_decibel5()
            self.add_record('sensor', 'location', 'home', 'decibel5', decibel5)
            
            pir5 = self.sensors.get_pir5()
            self.add_record('sensor', 'location', 'home', 'pir5', pir5)
            
            ultrasonic5 = self.sensors.get_ultrasonic5()
            self.add_record('sensor', 'location', 'home', 'ultrasonic5', ultrasonic5)
            
            temperature_pool_inside = self.sensors.get_temperature_pool_inside()
            self.add_record('sensor', 'location', 'home', 'temperature_pool_inside', temperature_pool_inside)
            

logger = Logger()
logger.run()
