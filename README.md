# home-automation

## Setup

### Install InfluxDB OSS v2:

[https://v2.docs.influxdata.com/v2.0/get-started/#start-with-influxdb-oss](https://v2.docs.influxdata.com/v2.0/get-started/#start-with-influxdb-oss)

```
$ wget https://dl.influxdata.com/influxdb/releases/influxdb_2.0.0-beta.16_linux_amd64.tar.gz
$ tar xvfz influxdb_2.0.0-beta.16_linux_amd64.tar.gz
$ sudo cp influxdb_2.0.0-beta.16_linux_amd64/{influx,influxd} /usr/local/bin/
```

Make service file for run on boot:

```
[Unit]
Description=InfluxDB OSS v2

[Service]
ExecStart=/usr/local/bin/influxd

[Install]
WantedBy=multi-user.target
```

Save it as /etc/systemd/system/influxd.service

```
$ sudo systemctl enable influxd.service
$ sudo systemctl start influxd.service
```

### Setup InfluxDB OSS v2:

```
$ influx setup
```

### Install requirements:

```
$ sudo apt-get install python3.7*
$ python3.7 -m pip install pip
$ git clone https://github.com/joosthoeks/home-automation.git
$ python3.7 -m pip install -r home-automation/requirements.txt
```

### Configuration:

Copy token from .influxdbv2/configs and paste it in home-automation/config.ini

### Add cronjobs:

```
$ crontab -e
```

```
@reboot sleep 60 && /usr/bin/python3.7 /home/USER/home-automation/logger.py &
@reboot sleep 70 && /usr/bin/python3.7 /home/USER/home-automation/controller.py &
```

### Reboot
