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

    def add_record(self, measurement, tag_key, tag_value, field_key, field_value, nanos):
        # https://v2.docs.influxdata.com/v2.0/reference/syntax/line-protocol/
        if isinstance(field_value, str):
            line = [
            '{},{}={} {}="{}" {}'
            .format(measurement, tag_key, tag_value, field_key, field_value, nanos)
            ]
        else:
            line = [
            '{},{}={} {}={} {}'
            .format(measurement, tag_key, tag_value, field_key, field_value, nanos)
            ]
        self.write_api.write(bucket=self.bucket, record=line)

    def run(self):

        while True:

            dummy0 = self.sensors.get_dummy_sensor0()
            self.add_record('sensor', 'location', 'home', 'dummy0', dummy0, time.time_ns())
            
            dummy1 = self.sensors.get_dummy_sensor1()
            self.add_record('sensor', 'location', 'home', 'dummy1', dummy1, time.time_ns())

            p1_esmr5 = self.sensors.get_p1_esmr5()
            nanos = time.time_ns()
            for k, v in p1_esmr5.items():
                self.add_record('p1', 'location', 'home', k, v, nanos)


            # reduce high cpu usage with sleep one microsecond:
#            time.sleep(.000001)
            # reduce high cpu usage with sleep one millisecond:
#            time.sleep(.001)


logger = Logger()
logger.run()
