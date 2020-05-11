""""""
# Import Built-Ins:
import json
from subprocess import PIPE, Popen

# Import Third-Party:

# Import Homebrew:


class Sensors:

    def __init__(self):
        pass

    def __bash(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        output, err = p.communicate()
        output = output.strip().decode(encoding='utf-8')
        err = err.strip().decode(encoding='utf-8')
#        return json.loads(output), err
        return output, err

    def get_dummy_sensor0(self):
        """
        read cpu temperature.
        """
        return int(self.__bash('cat /sys/class/thermal/thermal_zone0/temp')[0])

    def get_dummy_sensor1(self):
        """
        read cpu frequency.
        """
        return int(self.__bash('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')[0])

    # TODO
    def get_temperature_outside(self):
        return 0

    def get_humidity_outside(self):
        return 0

    def get_pressure_outside(self):
        return 0

    def get_light_outside(self):
        return 0

    def get_decibel_outside(self):
        return 0

    def get_temperature_pool_outside(self):
        return 0

    def get_wind(self):
        return 0

    def get_doorbell(self):
        return 0

    def get_temperature1(self):
        return 0

    def get_temperature2(self):
        return 0

    def get_temperature3(self):
        return 0

    def get_temperature4(self):
        return 0

    def get_temperature5(self):
        return 0

    def get_humidity1(self):
        return 0

    def get_humidity2(self):
        return 0

    def get_humidity3(self):
        return 0

    def get_humidity4(self):
        return 0

    def get_humidity5(self):
        return 0

    def get_pressure1(self):
        return 0

    def get_pressure2(self):
        return 0

    def get_pressure3(self):
        return 0

    def get_pressure4(self):
        return 0

    def get_pressure5(self):
        return 0

    def get_light1(self):
        return 0

    def get_light2(self):
        return 0

    def get_light3(self):
        return 0

    def get_light4(self):
        return 0

    def get_light5(self):
        return 0

    def get_decibel1(self):
        return 0
    
    def get_decibel2(self):
        return 0
    
    def get_decibel3(self):
        return 0
    
    def get_decibel4(self):
        return 0
    
    def get_decibel5(self):
        return 0
    
    def get_pir1(self):
        return 0

    def get_pir2(self):
        return 0

    def get_pir3(self):
        return 0

    def get_pir4(self):
        return 0

    def get_pir5(self):
        return 0

    def get_ultrasonic1(self):
        return 0

    def get_ultrasonic2(self):
        return 0

    def get_ultrasonic3(self):
        return 0

    def get_ultrasonic4(self):
        return 0

    def get_ultrasonic5(self):
        return 0

    def get_temperature_pool_inside(self):
        return 0

