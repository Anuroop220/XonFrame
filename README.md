
# XonFrame
XonFrame is an open-source smart glasses powered using ESP32-S3 and web app named XOSOFTWARE running E.L.I.X (The AI assistant for XonFrame)
My goal is to build smart glasses that are affordable and completely open source

They are open source and apparently they are smart too !

## Features

- Real time Navigation

- Live Camera feed

- Object detection

- Phone notifications

- Reminders

And we can talk to ELIX

The glasses mainly collect information and display results.

The phone handles speech recognition, computer vision, reasoning, navigation, and other AI features.

## HOW IT WORKS
The camera in the glasses capture frames when told and send it to xosoftware via wifi and ELIX looks at it and the question and answers the question !

## SCHEMATICS
<img width="2362" height="1672" alt="SCH_Schematic1_1-P1_2026-08-31" src="https://github.com/user-attachments/assets/b5c90973-1955-4134-8b41-e0af67420157" />

## 3D MODELS

                                         THIS IS THE CHARGING POD WERE THE TP4056 WILL BE THERE
<img width="512" height="243" alt="image" src="https://github.com/user-attachments/assets/30914196-cab9-4d4d-bf74-906e18a54e45" />

                                              THIS IS HOW THE GLASSES WILL LOOK LIKE  
<img width="512" height="274" alt="image" src="https://github.com/user-attachments/assets/fbc5e221-8b3b-4151-9df2-da2a4cc5a5ec" />

## PCB DESIGN

                                              THIS IS THE PCB DESIGN FOR THIS PROJECT
<img width="2160" height="723" alt="PCB_PCB1_2026-08-31 (1)" src="https://github.com/user-attachments/assets/1da3a379-82d9-4201-aadb-bf412fe403be" />

<img width="2160" height="723" alt="PCB_PCB1_2026-08-31 (2)" src="https://github.com/user-attachments/assets/ee24cc2e-bd19-43ba-89c0-83bde3ca7238" />



## BOM

| SL  NO | COMPONENT | QTY | VALUE  | PRICE | BUYING LINKS |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | ESP32-S3FH4R2 | 1 | - | $ 3.47  | [ESP32](https://www.lcsc.com/product-detail/C3013940.html?s_z=n_q_C3013940&globalKeyword=C3013940) |
| 2 | FPC CONNECTOR | 1 | - | $ 1.94  | [FPCCONNECTOR](https://www.lcsc.com/product-detail/C718080.html?s\_z=n\_q\_C718080\&globalKeyword=C718080) |
| 3 | 2.2nH INDUCTOR | 1 | 2.2nH | $ 0.03  | [INDUCTOR](https://www.lcsc.com/product-detail/C2044175.html?s_z=n_q_C2044175&globalKeyword=C2044175) |
| 4 | UFL CONNECTOR | 1 | - | $ 0.51  | [UFLCONNECTOR](https://www.lcsc.com/product-detail/C88374.html?s_z=n_q_C88374&globalKeyword=C88374) |
| 5 | 100uF | 1 | 100uF | $ 0.75  | [100uFCAPACITOR](https://www.lcsc.com/product-detail/C6882730.html?s_z=n_q_C6882730&globalKeyword=C6882730) |
| 6 | 1pF CAPCITOR | 2 | 1pF | ~ $0.0069  ($0.69 / 100 pcs)  | [1pFCAPACITOR](https://www.lcsc.com/product-detail/C277493.html?s_z=n_q_C277493&globalKeyword=C277493) |
| 7 | 100nF CAPACITOR | 8 | 100nF | ~ $0.0055 ($0.55 / 100 pcs)  | [100nFCAPACITOR](https://www.lcsc.com/product-detail/C1525.html?globalKeyword=C1525&s_z=n_q_C1525)  |
| 8 | 10uF CAPACITOR | 2 | 10uF | ~ $0.0258   ($2.58 / 100 pcs)  | [10uFCAPACITOR](https://www.lcsc.com/product-detail/C15525.html?s_z=n_q_C15525&globalKeyword=C15525) |
| 9 | 5.1kΩ RESISTOR | 2 | 5.1kΩ | ~ $ 0.0026   ($0.26 / 100 pcs) | [5.1kΩRESISTOR]((https://www.lcsc.com/product-detail/C25905.html?s_z=n_q_C25905&globalKeyword=C25905)  |
| 10 | 4.7kΩ RESISTOR | 2 | 4.7kΩ | ~ $ 0.0029    ($0.29 / 100 pcs) | [4.7kΩRESISTOR](https://www.lcsc.com/product-detail/C25900.html?s_z=n_q_C25900&globalKeyword=C25900) |
| 11 | 10kΩ RESISTOR | 3 | 10kΩ | ~ $ 0.0031    ($0.31 / 100 pcs) | [10kΩRESISTOR](https://www.lcsc.com/product-detail/C25744.html?s_z=n_q_C25744&globalKeyword=C25744) |
| 12 | AP2112K-3.3TRG1 3.3V LDO REGULATOR  | 1 | - | ~ $ 0.1777     ($0.89  / 5 pcs) | [3.3VLDO](https://www.lcsc.com/product-detail/C51118.html?s_z=n_q_C51118&globalKeyword=C51118)  |
| 13 | TYPE-C-31-M-12 16-PIN USB-C RECEPTACLE   | 1 | - | ~ $ 0.1716   ($0.86   / 5 pcs) | [USB-C](https://www.lcsc.com/product-detail/C165948.html?s_z=n_q_C165948&globalKeyword=C165948)  |
| 14 | USBLC6-2SC6 ESD PROTECTION DIODE ARRAY  | 1 | - | ~ $ 0.0449    ($0.45 / 10 pcs) | [USBLC6-2SC6](https://www.lcsc.com/product-detail/C2827654.html?s_z=n_q_C2827654&globalKeyword=C2827654)  |
| 15 | TS-1187A-B-A-B 5.1x5.1mm SMD TACTILE SWITCH  | 2 | - | ~ $ 0.0186    ($ 0.37 / 20 pcs) | [SMDSWITCH](https://www.lcsc.com/product-detail/C318884.html?s_z=n_q_C318884&globalKeyword=C318884) |
| 16 | BOSCH BMI270 IMU | 1 | - | $ 3.22  | [IMU](https://www.lcsc.com/product-detail/C2836813.html?s_z=n_q_C2836813&globalKeyword=C2836813)  |
| 17 | 2.54mm PITCH 1X2 MALE PIN HEADER  (ONE FOR CONNECTING THE BATTERY’S \+VE AND \- VE & THE OTHER ONE FOR CONNECTING THE AMPLIFIER BREAKOUT BOARD’S SPEAKER OUTPUT) | 2 | - | ~ $ 0.0299    ($0.60 / 20 pcs) | [1X2HEADERS](https://www.lcsc.com/product-detail/C124375.html?s_z=n_q_C124375&globalKeyword=C124375) |
| 18 | 2.54mm PITCH 1X3 MALE PIN HEADER  (BOTH ARE USED IN PLACE OF THE THE MIC’S PINS BECAUSE WE ARE USING INMP441 BREAKOUT BOARD) | 2 | - | ~ $ 0.0239    ($0.48 / 20 pcs)  | [1X3HEADERS](https://www.lcsc.com/product-detail/C52016391.html?s_z=n_q_C52016391&globalKeyword=C52016391) |
| 19 | 2.54mm PITCH 1X7 MALE PIN HEADER  (THIS IS USED AS IN PLACE OF THE AMPLIFIER’S 7 PINS) | 1 | - | ~ $ 0.0399    ($0.40 / 10 pcs)  | [1X7HEADERS](https://www.lcsc.com/product-detail/C5360900.html?s_z=n_q_C5360900&globalKeyword=C5360900) |
| 20 | 2.54mm PITCH 1X4 MALE PIN HEADER  (THIS IS USED AS IN PLACE OF THE DISPLAY’S 4 PINS) | 1 | - | ~ $ 0.0211    ($0.42 / 20 pcs) | [1X4HEADERS](http://lcsc.com/product-detail/C5116483.html?s_z=n_q_C5116483&globalKeyword=C5116483) |

                     


| COMPONENTS TO BE BOUGHT SEPARATELY *(BREAKOUT BOARDS,BATTERIES ETC*  |  |  |  |  |  |
| :---: | ----- | :---: | :---: | :---: | ----- |
| **SL NO** | **COMPONENT** | **QTY** | **VALUE** | **PRICE** | **BUYING LINKS** |
| 1 | INMP441 MEMS 12S MIC  | 1 | \- | $ 3.13 | \[INMP441MIC\]([https://www.amazon.in/DELLZO-INMP441-Digital-Microphone-Module/dp/B0GWM67TGW/ref=asc\_df\_B0GWM67TGW?mcid=700ca5ea755731658f8266bc54412566\&tag=googleshopdes-21\&linkCode=df0\&hvadid=709963085501\&hvpos=\&hvnetw=g\&hvrand=11666371826456957855\&hvpone=\&hvptwo=\&hvqmt=\&hvdev=c\&hvdvcmdl=\&hvlocint=\&hvlocphy=9149013\&hvtargid=pla-2479502317422\&hvocijid=11666371826456957855-B0GWM67TGW-\&hvexpln=0\&gad\_source=1\&th=1](https://www.amazon.in/DELLZO-INMP441-Digital-Microphone-Module/dp/B0GWM67TGW/ref=asc_df_B0GWM67TGW?mcid=700ca5ea755731658f8266bc54412566&tag=googleshopdes-21&linkCode=df0&hvadid=709963085501&hvpos=&hvnetw=g&hvrand=11666371826456957855&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9149013&hvtargid=pla-2479502317422&hvocijid=11666371826456957855-B0GWM67TGW-&hvexpln=0&gad_source=1&th=1))  |
| 2 | MAX98357 I2S 3W Class D Amplifier  | 1 | \- | $ 2.87 | \[MAX98357\]([https://www.amazon.in/MAX98357-Amplifier-Interface-Filterless-Raspberry/dp/B08XJSV2BH/ref=pd\_bxgy\_d\_sccl\_2/522-3421753-2679735?pd\_rd\_w=DdoYX\&content-id=amzn1.sym.142c0d31-3594-485b-b879-def9251f61c0\&pf\_rd\_p=142c0d31-3594-485b-b879-def9251f61c0\&pf\_rd\_r=E4FZPN5ES89JZA8HMPT1\&pd\_rd\_wg=hesBv\&pd\_rd\_r=27b9d194-edeb-439f-a3dc-9802dd739888\&pd\_rd\_i=B08XJSV2BH\&psc=1](https://www.amazon.in/MAX98357-Amplifier-Interface-Filterless-Raspberry/dp/B08XJSV2BH/ref=pd_bxgy_d_sccl_2/522-3421753-2679735?pd_rd_w=DdoYX&content-id=amzn1.sym.142c0d31-3594-485b-b879-def9251f61c0&pf_rd_p=142c0d31-3594-485b-b879-def9251f61c0&pf_rd_r=E4FZPN5ES89JZA8HMPT1&pd_rd_wg=hesBv&pd_rd_r=27b9d194-edeb-439f-a3dc-9802dd739888&pd_rd_i=B08XJSV2BH&psc=1)) |
| 3 | Waveshare 0.49inch 64×32 OLED Display   | 1 | \- | $ 5.96 | \[0.49INDISPLAY\]([https://robu.in/product/waveshare-0-49inch-oled-display-module-64x32-resolution-i2c-communication-black-white-display-color](https://robu.in/product/waveshare-0-49inch-oled-display-module-64x32-resolution-i2c-communication-black-white-display-color))  |
| 4 | 3.7V 450mAh Li-Po Rechargeable Battery (501035)  | 2 | \- | $4.08 | \[3.7VBATTERY\]([https://www.amazon.in/Rechargeable-501035-Lightweight-Earphones-Electroglobal/dp/B0G8G7PCJS?th=1](https://www.amazon.in/Rechargeable-501035-Lightweight-Earphones-Electroglobal/dp/B0G8G7PCJS?th=1)) |
| 5 | GSM FPC (Flexible) Antenna \-1.5 dBi with UFL (IPEX) Connector  | 1 | \- | \~ $ 0.60 | \[PIGTAILANTENNA\]([https://evelta.com/gsm-fpc-flexible-antenna-1-5-dbi-with-ufl-ipex-connector](https://evelta.com/gsm-fpc-flexible-antenna-1-5-dbi-with-ufl-ipex-connector)) |
| 6 | OV5640 Camera Module 5MP 68° HFOV MIPI 24-pin FPC  | 1 | \- | $ 9.42 | \[OV5640CAMERA\]([https://www.amazon.in/dp/B0HCYQJ8L3?ref=cm\_sw\_r\_cp\_ud\_dp\_D0MHWPTRH4WZW4WZHY7F\&ref\_=cm\_sw\_r\_cp\_ud\_dp\_D0MHWPTRH4WZW4WZHY7F\&social\_share=cm\_sw\_r\_cp\_ud\_dp\_D0MHWPTRH4WZW4WZHY7F](https://www.amazon.in/dp/B0HCYQJ8L3?ref=cm_sw_r_cp_ud_dp_D0MHWPTRH4WZW4WZHY7F&ref_=cm_sw_r_cp_ud_dp_D0MHWPTRH4WZW4WZHY7F&social_share=cm_sw_r_cp_ud_dp_D0MHWPTRH4WZW4WZHY7F)) |
| 7 | TP4056 C TYPE Charging Module  | 1 | \- | $ 0.68 | \[TP4056\]([https://www.amazon.in/UNIVERSAL-HUB-TP4056-Overcharge-Protection/dp/B0FVLYQBKC?source=ps-sl-shoppingads-lpcontext\&ref\_=fplfs\&smid=A366YFPXO3CTI5\&th=1](https://www.amazon.in/UNIVERSAL-HUB-TP4056-Overcharge-Protection/dp/B0FVLYQBKC?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A366YFPXO3CTI5&th=1)) |
| 8 | Exciter 8Ω 1W Bone conduction speaker  | 1 | \- | \~ $7.43  | \[SPEAKER\]([https://www.thingbits.in/products/bone-conductor-transducer-with-wires-8-ohm-1-watt?srsltid=AfmBOopAAxpBy44V6buE1m6lCgi68V1ijIYXX552VQ8EoFbC07jLNLEY](https://www.thingbits.in/products/bone-conductor-transducer-with-wires-8-ohm-1-watt?srsltid=AfmBOopAAxpBy44V6buE1m6lCgi68V1ijIYXX552VQ8EoFbC07jLNLEY)) |

## TUTORIAL ON BUILDING !
Download XonFrame Repository
Clone or download the repository.
Folders/Files -
 3D MODELS/
 BOM/
 Firmware/
 Pcb/
 Software/
 README.md
 
**Order the PCB**

Go to the PCB folder

You will find the GERBER ZIP and much more

And in BOM folder you will find the BOM file

After getting this files

Go to [JLCPCB](https://jlcpcb.com/)

Click Order now 

<img width="512" height="274" alt="image" src="https://github.com/user-attachments/assets/fcc1a500-2c94-4a3c-99d4-8c0e0b1a3d12" />

Then upload the provided XonFrame_Gerbers.zip here

<img width="512" height="146" alt="image" src="https://github.com/user-attachments/assets/5de2c32e-1b36-44db-ab4c-12c93bbe6a01" />


**PCB Settings**

For this pcb use this settings 

<img width="512" height="232" alt="image" src="https://github.com/user-attachments/assets/823daee0-f3c7-427a-a985-6fd204ad4446" />

<img width="512" height="328" alt="image" src="https://github.com/user-attachments/assets/d125c171-de91-45c4-84df-fffea2c8c953" />

<img width="512" height="333" alt="image" src="https://github.com/user-attachments/assets/cc8c847e-2d82-4dac-871f-dc53e9433ffa" />

<img width="512" height="327" alt="image" src="https://github.com/user-attachments/assets/f336620b-afed-479a-b457-2e868a71f4a4" />


**PCB Assembly**

While Ordering the pcb just turn on the Pcb Assembly option


<img width="512" height="297" alt="image" src="https://github.com/user-attachments/assets/3d4501cc-a060-4ffd-9976-d744e4e16b8f" />

AFTER THAT -
<img width="512" height="159" alt="image" src="https://github.com/user-attachments/assets/cf318b42-ddc6-423e-b288-1ffe8141734d" />


CLICK NEXT 
THEN-  YOU WILL BE IN DIRECTED TO THIS PAGE 


<img width="512" height="181" alt="image" src="https://github.com/user-attachments/assets/5802c3e3-2952-4e07-88d4-b3c881d86da3" />


AND IN HERE CLICK THIS 

<img width="512" height="129" alt="image" src="https://github.com/user-attachments/assets/d717aa59-ce62-43bb-98d8-931657ec1278" />

AND UPLOAD THE BOM AND CPL FILES PROVIDED IN THE BOM FOLDER IN HERE

<img width="512" height="122" alt="image" src="https://github.com/user-attachments/assets/682ecd1d-7fc0-406d-a138-8b036790cc7d" />

NEXT YOU WILL GET TO THIS PAGE AND THEN MAKE SURE EVERY COMPONENT IS SELECTED OR JUST CLICK SELECT ALL IT IS MARKED IN THE PIC BELOW

<img width="512" height="124" alt="image" src="https://github.com/user-attachments/assets/3c9d4b89-a69f-469e-96ef-be97d4a4847d" />
 
THEN IN THE FOLLOWING PAGE CLICK ADD TO CART AND AFTER THAT BUY IT

 **3D Printing the Frame**

Go to 3D MODELS/

Then Upload the STL files.

***(Do not resize them)***

Set the model Scale to 100%

**Settings to use**

| Material | PETG |
| :---- | :---- |
| Layer height | 0.16 \- 0.20 mm |
| walls | 3 |
| infill | 15 \- 25 % |
| nozzle | 0.4mm |
| Support  | Only when needed |

Installing Arduino IDE 
Install Arduino IDE  from [INSTALL ARDUINO IDE](https://www.arduino.cc/en/software/?_gl=1*8okl3v*_up*MQ..*_ga*OTAwMTg5ODk1LjE3ODcwNDMwNzk.*_ga_NEXN8H46L5*czE3ODcwNDMwNzkkbzEkZzAkdDE3ODcwNDMwNzkkajYwJGwwJGgyNTEzNDEwNTY.)
Then install the ESP32 board package 
File - Preferences - and in additional board manager urls 
PASTE THIS https://espressif.github.io/arduino-esp32/package_esp32_index.json

<img width="512" height="231" alt="image" src="https://github.com/user-attachments/assets/19b51bf7-56ca-44d4-9153-489220b85125" />


AFTER THAT -
Search  ESP32  in the Boards Manager tab 

<img width="392" height="440" alt="image" src="https://github.com/user-attachments/assets/93c3ffd2-f593-4f45-ad3c-e78dabef1454" />


and install 
esp32 by espressif systems

<img width="238" height="202" alt="image" src="https://github.com/user-attachments/assets/3537b2c4-8ad4-484b-8cbd-1c1fb025e244" />

Arduino IDE Board Configuration

ESP32-S3FH4R2 is a bare chip, not a devkit so we need to change the default configuration for that  first select the board
Search  ESP32S3 dev module select ESP32S3 Dev Module (we should not select the Octal (WROOM2) one  we should select the normal one) 
Then in Tools menu Scroll down  Then use these configurations -

<img width="478" height="512" alt="image" src="https://github.com/user-attachments/assets/1fe6c573-797f-4af0-9e17-e5582842f1db" />

After that 
Select the COM port 
Tools - Port

Arduino IDE Libraries

NEXT WE NEED TO INSTALL THE LIBRARIES  SO THESE ARE THE ONES WE SHOULD INSTALL AND WHILE INSTALLING IF ASKED ABOUT INSTALLING DEPENDENCIES IT SHOULD BE INSTALLED TOO  

<img width="257" height="267" alt="image" src="https://github.com/user-attachments/assets/a5e727c4-f034-455d-932f-cae2949906c3" />
<img width="250" height="237" alt="image" src="https://github.com/user-attachments/assets/bdc5ebc7-611e-4165-8bee-86d364282c89" />
<img width="282" height="269" alt="image" src="https://github.com/user-attachments/assets/89383a0b-24b6-4c1c-a400-98d6159c48e8" />


Now for Configuring wifi 


Replace this part with your wifi name and password

#define WIFI_SSID "YOUR_WIFI"

#define WIFI_PASSWORD "YOUR_PASSWORD"

And after doing all this click upload and it will be flashed into the ESP32


**ELIX**


For using ELIX we need python for that first install Python

Go to the folder path in the terminal

using  the command    

cd pathtothefolder 

Now for installing the dependences 

Type  -   pip install requirements.txt



**API KEYS** 


API keys are needed for the maps,messages and elix

So for that 

FIRST GET THE API KEYS FROM THE FOLLOWING SERVICES

GEMINI API - [GOOGLEAISTUDIO](https://aistudio.google.com)

ORS API - [OPENROUTESERVICE](https://openrouteservice.org)

PUSHBULLET API - [PUSHBULLET API](https://www.pushbullet.com)

After getting the keys we need to put them in the .env file

The repo already has a file called

.env.example

First we should copy the contents in that file and then make a new txt file in the same software folder that we are currently in.And paste the content  of .env.example.

NEXT fill the empty spaces were API is to be filled with API and save it 
 
And after saving the rename the file to .env

For example - GEMINI_API_KEY=  APIKEY12345



FOR TESTING ELIX (laptop) 


 To test ELIX keep elix_bridge.py running while using the xosoftware and main.py

start it in another terminal by typing python elix_bridge.py 

(it works like at first go to to the folder path then type python main.py

in the first window and next create a second window and type

python elix_bridge.py and both should be running along side the xosoftware in the browser)

use this bridge URL in the xosoftware settings tab

http://<paste_laptop_ip_here>:5001

if it is running in the same computer where the xosofware is running 

 use this ip  http://localhost:5001

 it will be already there so no need to change

---

## Contributing

If you have ideas, find a bug, or want to help building XonFrame, feel free to open an issue or submit a pull request.

Whether it's firmware, hardware, documentation, or design every contributions are welcome

## License

Software is licensed under Apache 2.0.

Hardware designs are licensed under CERN-OHL-W-2.0.


by Anuroop
