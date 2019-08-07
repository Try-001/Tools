#!/bin/bash
#!/bin/bash
username=admin
password=Admin123
IP=`ip a| grep inet | grep -v 'inet6\|127.0.0.1' | awk '{print $2}' | awk -F / '{print $1}'`
edition=`cat /etc/redhat-release | awk '{print $4}' | awk -F . '{print $1}'`

cat > /etc/yum.repos.d/influxdb.repo << END
[influxdb]
name = InfluxDB Repository - RHEL \$releasever
baseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
END

yum -y install influxdb
yum -y install telegraf
mv /etc/telegraf/telegraf.conf /etc/telegraf/telegraf.conf.bac

cat > /etc/telegraf/telegraf.conf << END

[global_tags]
[agent]
  interval = "30s"
  round_interval = true
  metric_batch_size = 1000
  metric_buffer_limit = 10000
  collection_jitter = "0s"
  flush_interval = "10s"
  flush_jitter = "0s"
  precision = ""
  hostname = "influxdb"
  omit_hostname = false
[[inputs.cpu]]
  percpu = true
  totalcpu = true
  collect_cpu_time = false
  report_active = false
[[inputs.disk]]
  ignore_fs = ["tmpfs", "devtmpfs", "devfs", "iso9660", "overlay", "aufs", "squashfs"]
[[inputs.diskio]]
[[inputs.kernel]]
[[inputs.mem]]
[[inputs.processes]]
[[inputs.swap]]
[[inputs.system]]
[[inputs.influxdb]]
  urls = ["http://$IP:8086/debug/vars"]
 
[[outputs.influxdb]]
  urls = ["http://$IP:8086/debug/vars"]
  database = "telegraf"
  skip_database_creation = false
  timeout = "5s"
  username = "admin"
  password = "Admin123"
 
[[outputs.prometheus_client]]
   listen = ":9273"
END

if [ "$edition" == 7 ]
then
        systemctl start influxdb
	systemctl start telegraf
else
        service influxdb start
	service telegraf start
fi