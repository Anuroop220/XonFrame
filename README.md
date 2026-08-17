# XonFrame
XonFrame is an open-source smart glasses powered using ESP32-S3 and phone app running E.L.I.X (The AI assistant for XonFrame)

My goal is to build smart glasses that are affordable repairable and completely open source.

## Features

Real time Navigation

Live Camera feed

Object detection

Phone notifications

Reminders

And we can talk to ELIX

The glasses mainly collect information and display results.

The phone handles speech recognition, computer vision, reasoning, navigation, and other AI features.

## Components Needed

ESP32-S3FH4R2

OV5640 Camera module

0.49in SSD1306 OLED display

INMP441 12s Microphone

Exciter 8Ω 1W Bone conduction speaker

BM1270 6 Axis IMU

2x 350 mAh 3.7v (501035) LiPo Rechargeable battery 

Safety Important - Both 3.7v batteries must be at the exact same voltage (both fully charged to 4.2v) during the very first time when soldering them together in parallel or high currents will flow between them
 
## BOM
No.	Quantity	Comment	Designator	Footprint	Value	Manufacturer Part	Manufacturer	Supplier Part	Supplier
1	1	2.54-1*4	0.49in-Display	HDR-TH_4P-P2.54-V-M-1		2.54-1*4	ZHOURI(洲日)	C5116483	LCSC
2	1	ANT_2.4G	ANT1	RF-SMD_FRF05002-JSS103M	ANT_2.4G	U.FL-R-SMT-1(80)	HRS(广濑)		LCSC
3	1	100uF	C1	C0805	100uF	CL21A107MQYNNWE	SAMSUNG(三星)	C6882730	LCSC
4	8	100nF	C2,C5,C6,C7,C8,C9,C10,C11	C0402	100nF	CL05B104KO5NNNC	SAMSUNG(三星)	C1525	LCSC
5	2	10uF	C3,C4	C0402	10uF	CL05A106MQ5NUNC	SAMSUNG(三星)	C15525	LCSC
6	2	1pF	C14,C15	C0402	1pF	CC0402CRNPO9BN1R0	YAGEO(国巨)	C277493	LCSC
7	1	USBLC6-2SC6	D2	SOT-23-6_L2.9-W1.6-P0.95-LS2.8-BL		USBLC6-2SC6	TECH PUBLIC(台舟)	C2827654	LCSC
8	1	FPC05024-17205	FPC2	FPC-SMD_FPC05024-17205		FPC05024-17205	ATOM(爱特姆)	C718080	LCSC
9	2	B-2100S02P-A110	H1,SP-INPUT1	HDR-TH_2P-P2.54-V-M-1		B-2100S02P-A110	Ckmtw(灿科盟)	C124375	LCSC
10	1	2.2nH	L1	L0402	2.2nH	MHQ1005P2N2CT000	TDK	C2044175	LCSC
11	2	HX PH254-01-03-Z-L11.5 pcb pin header	MIC1-LWS,MIC2-GVS	HDR-TH_3P-P2.54-V-M-1		HX PH254-01-03-Z-L11.5 pcb pin header	hanxia(韩下)	C52016391	LCSC
12	2	4.7kΩ	R1,R6	R0402	4.7kΩ	0402WGF4701TCE	UNI-ROYAL(厚声)	C25900	LCSC
13	3	10kΩ	R2,R3,R4	R0402	10kΩ	0402WGF1002TCE	UNI-ROYAL(厚声)	C25744	LCSC
14	2	5.1kΩ	R7,R8	R0402	5.1kΩ	0402WGF5101TCE	UNI-ROYAL(厚声)	C25905	LCSC
15	2	TS-1187A-B-A-B	SW1,SW2	SW-SMD_4P-L5.1-W5.1-P3.70-LS6.5-TL_H1.5		TS-1187A-B-A-B	XKB Connection(中国星坤)	C318884	LCSC
16	1	BMI270	U2	LGA-14_L3.0-W2.5-P0.50-BR		BMI270	Bosch(博世)	C2836813	LCSC
17	1	PZ2.54-1*7	U4	HDR-TH_7P-P2.54-V-M		PZ2.54-1*7	ZHOURI(洲日)	C5360900	LCSC
18	1	AP2112K-3.3TRG1	U6	SOT-25-5_L2.9-W1.6-P0.95-LS2.8-BL		AP2112K-3.3TRG1	DIODES(美台)	C51118	LCSC
19	1	2.4GHz	U7	QFN-56_L7.0-W7.0-P0.40-BL-EP5.7	2.4GHz	ESP32-S3FH4R2	ESPRESSIF(乐鑫)	C3013940	LCSC
20	1	TYPE-C-31-M-12	USBC1	USB-C_SMD-TYPE-C-31-M-12_1		TYPE-C-31-M-12	韩国韩荣	C165948	LCSC

[Mouser](https://www.mouser.in/en/ProductDetail/Espressif-Systems/ESP32-S3FH4R2?qs=tlsG%2FOw5FFjPrwkmZSBQNA%3D%3D&srsltid=AfmBOoqKYVMap9jSj9ATa5MjMtgFBaLuwApidHaJJ7h-9lh4Gxkn0UCc)


## Software

Python
OpenCV
YOLO
ESP-IDF / Arduino

## TUTORIAL ON BUILDING THIS ! 
So for that first go to the PCB folder then take all the files and then go to JLC PCB
## Why I'm building this

I am building this because most smart glasses are expensive, closed source and difficult to modify.

I wanted to build something that anyone could build, improve, or even build themselves.

XonFrame is my idea to make smart glasses more open and accessible


## Contributing

If you have ideas, find a bug, or want to help building XonFrame, feel free to open an issue or submit a pull request.

Whether it's firmware, hardware, documentation, or design every contribution is welcome.

## License

Software is licensed under Apache 2.0.

Hardware designs are licensed under CERN-OHL-W-2.0.


by Anuroop
