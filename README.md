# backlog-cmd-gen
## How to use
- Copy `example-config.yml` and rename to `config.yml`.
- Fill out fields in `config.yml` with the correct values for your device. For sections like the template and NTP settings, consult the Tasmota documentation [here](https://tasmota.github.io/docs/).
- Save the `config.yml` file and run `python3 cmd-gen.py`.
- Copy the output and paste it into the Tasmota console.

Note: these are the settings that needed to be changed for my particular devices, your application may need different commands to change different settings. 