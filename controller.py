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
from actions import Actions


if sys.version_info < (3, 7, 0):
    sys.exit('Python 3.7.0 or higher is required. You are using Python {}.{}.{}.'.format(sys.version_info[0], sys.version_info[1], sys.version_info[2]))


class Controller:

    def __init__(self):
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_file)
        client = InfluxDBClient.from_config_file(config_file)
        self.query_api = client.query_api()
        self.bucket = config['ha']['influx_bucket']
        self.actions = Actions()

    def get_last_record(self, measurement, tag_key, tag_value, field_key):
        # https://v2.docs.influxdata.com/v2.0/query-data/get-started/query-influxdb/
        query = '''
        from(bucket:"{}")
        |> range(start: -10d)
        |> filter(fn:(r) => r._measurement == "{}")
        |> filter(fn: (r) => r.{} == "{}")
        |> filter(fn:(r) => r._field == "{}")
        |> last()
        '''.format(self.bucket, measurement, tag_key, tag_value, field_key)

        result = self.query_api.query(query=query)
        return result[0].records[0]

    def run(self):

        while True:

            last_value = self.get_last_record('sensor', 'location', 'home', 'dummy0')['_value']
            if last_value > 80000:
                self.actions.do_action1()
            if last_value < 60000:
                self.actions.do_action2()


controller = Controller()
controller.run()
