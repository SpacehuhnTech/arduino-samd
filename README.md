# SAMD Arduino Core for WiFi Duck Project

This repository is a fork of the [Adafruit SAMD Arduino Core](https://github.com/adafruit/ArduinoCore-samd) to include libraries, boards and modifications necessary to compile the [WiFi Duck](https://github.com/spacehuhntech/wifiduck) project.  
The goal of this is to have a simpler installation setup for anyone that likes to test, modify and contribute to the wifi duck project.  

## License and credits

Arduino IDE is developed and maintained by the Arduino team. The IDE is licensed under GPL.

## Modifications

* Replaced `cores/arduino` with `cores/arduino` from [Arduino SAMD core](https://github.com/arduino/ArduinoCore-samd)
* Replaced `libraries` with `libraries` from [Arduino SAMD core](https://github.com/arduino/ArduinoCore-samd)
* Added boards.txt.py, modified boards.txt and platform.txt to add WiFi Duck boards and change default values
