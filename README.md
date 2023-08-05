# backlog-cmd-gen
## How to use
- Install Tasmota on your device using the [webinstaller](https://tasmota.github.io/install/).
- Once it installs, click "Next", then skip WiFi setup.
- Click "Logs & Console" to open the Tasmota console.
- Clone this repo with `git clone https://github.com/Darkextratoasty/Tasmota-Setup-Command-Generator.git`.
- cd into `Tasmota-Setup-Command-Generator`.
- Copy `example-config.yml` and rename to `config.yml`.
- Fill out fields in `config.yml` with the correct values for your device. For sections like the template and NTP settings, consult the Tasmota documentation [here](https://tasmota.github.io/docs/).
- Save the `config.yml` file and run `python3 cmd-gen.py`.
- Copy the output and paste it into the Tasmota console.
- Wait a few minutes for everything to run.

Note: these are the settings that needed to be changed for my particular devices, your application may need different commands to change different settings. 
