import yaml

with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
        cmd = "Backlog SSId1 " + config['wifi_ssid']
        cmd += "; Password " + config['wifi_password']
        cmd += "; Hostname " + config['device_hostname']
        cmd += "; MqttHost " + config['mqtt_host']
        cmd += "; MqttPort " + config['mqtt_port']
        cmd += "; MqttUser " + config['mqtt_username']
        cmd += "; MqttPassword " + config['mqtt_password']
        cmd += "; Topic " + config['mqtt_topic']
        cmd += "; DeviceName " + config['device_name']
        if config['configure_ntp']:
            cmd += "; NtpServer1 " + config['ntp_server']
            cmd += "; Timezone " + config['ntp_timezone']
            cmd += "; TimeStd " + config['ntp_timestd']
            cmd += "; TimeDst " + config['ntp_timedst']
        cmd += "; Template " + config['template']
        cmd += "; SetOption8 1"
        cmd += "; Module 0"

        print(cmd)
    except yaml.YAMLError as exc:
        print(exc)
