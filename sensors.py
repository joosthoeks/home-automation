""""""
# Import Built-Ins:
import json
from subprocess import PIPE, Popen

# Import Third-Party:
import serial

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
        return float(self.__bash('cat /sys/class/thermal/thermal_zone0/temp')[0])

    def get_dummy_sensor1(self):
        """
        read cpu frequency.
        """
        return float(self.__bash('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')[0])

    def get_p1_esmr5(self):
        """
        read smart meter DSMR P1 XS210 ESMR 5.0
        source: https://www.netbeheernederland.nl/_upload/Files/Slimme_meter_15_a727fce1f1.pdf
        """
        p1_dict = {}
        with serial.Serial('/dev/ttyUSB0') as ser:
            ser.baudrate = 115200
            ser.bytesize = serial.EIGHTBITS
            ser.parity = serial.PARITY_NONE
            ser.stopbits = serial.STOPBITS_ONE
#            ser.port = '/dev/ttyUSB0'
#            ser.open()
            i = 0
            while i < 26:
                p1_raw = ser.readline()
                p1_str = str(p1_raw)
                p1_line = p1_str.strip()
                # Equipment identifier:
                if p1_line[2:12] == '0-0:96.1.1':
                    p1_dict[p1_line[2:12]] = int(p1_line[13:47])
                # Meter Reading electricity delivered to client (low tariff) in 0,001 kWh:
                if p1_line[2:11] == '1-0:1.8.1':
                    p1_dict[p1_line[2:11]] = float(p1_line[12:22])
                # Meter Reading electricity delivered to client  (normaltariff) in 0,001 kWh:
                if p1_line[2:11] == '1-0:1.8.2':
                    p1_dict[p1_line[2:11]] = float(p1_line[12:22])
                # Meter Reading electricity delivered by client  (lowtariff) in 0,001 kWh:
                if p1_line[2:11] == '1-0:2.8.1':
                    p1_dict[p1_line[2:11]] = float(p1_line[12:22])
                # Meter Reading electricity delivered by client  (normaltariff) in 0,001 kWh:
                if p1_line[2:11] == '1-0:2.8.2':
                    p1_dict[p1_line[2:11]] = float(p1_line[12:22])
                # Tariff indicator electricity. The tariff indicator can be used to switch tariff dependent loads e.g boilers. This is responsibility of the P1 user:
                if p1_line[2:13] == '0-0:96.14.0':
                    p1_dict[p1_line[2:13]] = int(p1_line[14:18])
                # Actual electricity power delivered (+P) in 1 Watt resolution:
                if p1_line[2:11] == '1-0:1.7.0':
                    p1_dict[p1_line[2:11]] = float(p1_line[12:18])
                # Actual electricity power received (-P) in 1 Watt resolution:
                if p1_line[2:11] == '1-0:2.7.0':
                    p1_dict[p1_line[2:11]] = float(p1_line[12:18])
                # Number of power failures in any phases:
                if p1_line[2:13] == '0-0:96.7.21':
                    p1_dict[p1_line[2:13]] = int(p1_line[14:19])
                # Number of long power failures in any phases:
                if p1_line[2:12] == '0-0:96.7.9':
                    p1_dict[p1_line[2:12]] = int(p1_line[13:18])
                # Power failure event log:
                if p1_line[2:13] == '1-0:99.97.0':
                    p1_dict[p1_line[2:13]] = str(p1_line[13:-5])
                # Number of voltage sags in phase L1:
                if p1_line[2:13] == '1-0:32.32.0':
                    p1_dict[p1_line[2:13]] = int(p1_line[14:19])
                # Number of voltage swells in phase L1:
                if p1_line[2:13] == '1-0:32.36.0':
                    p1_dict[p1_line[2:13]] = int(p1_line[14:19])
                # Instantaneous voltage L1:
                if p1_line[2:12] == '1-0:32.7.0':
                    p1_dict[p1_line[2:12]] = float(p1_line[13:18])
                # Instantaneous current L1:
                if p1_line[2:12] == '1-0:31.7.0':
                    p1_dict[p1_line[2:12]] = float(p1_line[13:16])
                # Instantaneous active power L1 (+P):
                if p1_line[2:12] == '1-0:21.7.0':
                    p1_dict[p1_line[2:12]] = float(p1_line[13:19])
                # Instantaneous active power L1 (-P):
                if p1_line[2:12] == '1-0:22.7.0':
                    p1_dict[p1_line[2:12]] = float(p1_line[13:19])
                # Text message max 1024 characters.
                if p1_line[2:13] == '0-0:96.13.0':
                    p1_dict[p1_line[2:13]] = str(p1_line[13:-5])
                # Device-Type:
                if p1_line[2:12] == '0-1:24.1.0':
                    p1_dict[p1_line[2:12]] = int(p1_line[13:16])
                # Equipment identifier:
                if p1_line[2:12] == '0-1:96.1.0':
                    p1_dict[p1_line[2:12]] = int(p1_line[13:47])
                # Last 5-minutevalue(temperature converted), gas delivered to client in m3, including decimal valuesand capture time:
                if p1_line[2:12] == '0-1:24.2.1':
                    p1_dict[p1_line[2:12]] = float(p1_line[28:37])
                i += 1
            return p1_dict
