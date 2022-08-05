<h1 align="center">NeoPicoJiggler</h1>

<div align="center">
  <strong>Make a nice mouse jiggler with a NeoPixel control</strong>
</div>

<br />

<div align="center">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/MoHorst/NeoPicoJiggler">
  <img alt="GitHub license" src="https://img.shields.io/github/license/MoHorst/NeoPicoJiggler">
  <a href="https://github.com/MoHorst/NeoPicoJiggler/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/MoHorst/NeoPicoJiggler"></a>
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/MoHorst/NeoPicoJiggler">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/MoHorst/NeoPicoJiggler">
</div>

<br />

## Install

Install and have your NeoPicoJiggler working in less than 5 minutes.

1. Download [CircuitPython for the Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/). *Updated to 7.0.0

2. Plug the device into a USB port while holding the boot button. It will show up as a removable media device named `RPI-RP2`.

3. Copy the downloaded `.uf2` file to the root of the Pico (`RPI-RP2`). The device will reboot and after a second or so, it will reconnect as `CIRCUITPY`.

4. Download `adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip` [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest) and extract it outside the device.

5. Navigate to `lib` in the recently extracted folder and copy `adafruit_hid` to the `lib` folder in your Raspberry Pi Pico.

6. Click [here](https://raw.githubusercontent.com/dbisu//MoHorst/NeoPicoJiggler/code.py), press CTRL + S and save the file as `code.py` in the root of the Raspberry Pi Pico, overwriting the previous file.

### NeoPixel
1. connect NeoPixel din to Pin 1
![Prototyp](images/NeoPicoJiggler.png)
2 copy neopixel.mpy to `lib`.


#### USB enable/disable mode

If you need the NeoPicoJiggler to not show up as a USB mass storage device for stealth, follow these instructions.  
Enter setup mode.  
Copy boot.py to the root of the NeoPicoJiggler.  
Disconnect the pico from your host PC.
Connect a jumper wire between pin 18 (`GND`) and pin 20 (`GPIO15`).
This will prevent the NeoPicoJiggler from showing up as a USB drive when plugged into the target computer.  
Remove the jumper and reconnect to your PC to reprogram.
The default mode is USB mass storage enabled.   

![USB enable/disable mode](images/usb-boot-mode.png)
