# home-automation

## Setup

```
$ git clone https://github.com/joosthoeks/home-automation.git
```

### Install InfluxDB OSS v2 and InfluxDB Python Client:

[https://v2.docs.influxdata.com/v2.0/get-started/#start-with-influxdb-oss](https://v2.docs.influxdata.com/v2.0/get-started/#start-with-influxdb-oss)

```
$ wget https://dl.influxdata.com/influxdb/releases/influxdb_2.0.0-beta.10_linux_amd64.tar.gz
$ tar xvfz influxdb_2.0.0-beta.10_linux_amd64.tar.gz
$ sudo cp influxdb_2.0.0-beta.10_linux_amd64/{influx,influxd} /usr/local/bin/
```

Make organisation: "test"
Make bucket: "test"

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

[https://github.com/influxdata/influxdb-client-python](https://github.com/influxdata/influxdb-client-python)

```
$ sudo pip3 install influxdb-client
```

### Add cronjobs:

```
$ crontab -e
```

```
@reboot sleep 60 && /usr/bin/python3 /home/USER/home-automation/logger.py &
@reboot sleep 60 && /usr/bin/python3 /home/USER/home-automation/controller.py &
```
