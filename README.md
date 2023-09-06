## Freenove Robot Dog Kit for Raspberry Pi for IVE Final Year Project

> A Robot Dog Kit for Raspberry Pi.

<img src='Picture/icon.png' width='30%'/>

### Important Reminder 
Don't upgrade Pi-OS!!! Else it will crash and need to reinstall Pi-OS and everything

### How to Setup? (In case Factory ReSet)
ping -4 raspberrypi.local
setup pi
cd ~
git clone https://github.com/kitson618/IVE_Robot_Dog_Kit_for_Pi.git
cd ~/IVE_Robot_Dog_Kit_for_Pi/Code
sudo python setup.py
sudo raspi-config

* sudo nano /boot/config.txt
dtparam=i2c_arm=on, and add “i2c_arm_baudrate=400000”.
dtoverlay=vc4-fkms-v3d,cma-320
dtoverlay=OV5647
gpu_mem=128
start_x=1

* sudo nano /etc/modules
bcm2835-v4l2

keep 90
cd ~/IVE_Robot_Dog_Kit_for_Pi/Code/Server
sudo python Servo.py

* Upgrade Python Library
sudo apt install -y python3-libcamera python3-kms++
sudo apt install -y python3-pyqt5 python3-prctl libatlas-base-dev ffmpeg python3-pip
pip3 install numpy --upgrade
pip3 install picamera2[gui]
pip install picamera2==0.3.12


* Test
cd ~/Freenove_Robot_Dog_Kit_for_Raspberry_Pi/Code/Server
sudo python test.py Servo
**voltage**
sudo python test.py ADC
**Ultrasonic**
sudo python test.py Ultrasonic
**LED**
sudo python test.py Led
**Buzzer**
sudo python test.py Buzzer

* Camera test
libcamera-hello

* take photo
python camera.py
libcamera-still -o test.jpg

* check camera state
vcgencmd get_camera
v4l2-ctl --list-devices

* Run the server in Robot Dog 
sudo python main.py

### Current setup Specification

* Model : Raspberry Pi - 4B, 8 GB version
* Camera Module : picamera2 (0.3.12)
* Python Version 3.9.2:
* OS : Release date: May 3rd 2023, System: 32-bit, Kernel version: 6.1, Debian version: 11 (bullseye)
* Camera :  robot dog - 5MP one (OV5647)
* Added dtoverlay=OV5647 to config.txt
* Disabled legacy camera from raspi-config

### Orginial Source

* **Use command in console**

	Run following command to download all the files in this repository.

	`git clone https://github.com/Freenove/Freenove_Robot_Dog_Kit_for_Raspberry_Pi.git`


### Copyright

All the files in this repository are released under [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/).

![markdown](https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)

This means you can use them on your own derived works, in part or completely. But NOT for the purpose of commercial use.
You can find a copy of the license in this repository.

Freenove brand and logo are copyright of Freenove Creative Technology Co., Ltd. Can't be used without formal permission.


### About

Freenove is an open-source electronics platform.

Freenove is committed to helping customer quickly realize the creative idea and product prototypes, making it easy to get started for enthusiasts of programing and electronics and launching innovative open source products.

Our services include:

* Robot kits
* Learning kits for Arduino, Raspberry Pi and micro:bit
* Electronic components and modules, tools
* Product customization service

Our code and circuit are open source. You can obtain the details and the latest information through visiting the following web site:

http://www.freenove.com
