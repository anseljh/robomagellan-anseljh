# robomagellan-anseljh

This repo has notes, code, and other stuff related to my work toward competing in a Robo-Magellan contest. I plan to do at least the [TableBot challenge](https://github.com/anseljh/tablebot) first, but I've started planning and collecting parts for Robo-Magellan. I hope to be ready to compete in spring/summer 2024, but that may be overly ambitious. 2025 for sure!

## Robo-Magellan

> Robo-Magellan is a robotics competition emphasizing autonomous navigation and obstacle avoidance over varied, outdoor terrain. Robots have three opportunities to navigate from a starting point to an ending point and are scored on time required to complete the course with opportunities to lower the score based on contacting intermediate points.

- RoboGames [Robo-Magellan Rules](http://robogames.net/rules/magellan.php)
- Seattle Robotic Society Robothon [Robo-Magellan Rules](https://robothon.org/rules-robo-magellan/)

## Design Considerations

- **Size**: The robot will need to be able to overcome some terrain obstacles, so it shouldn't be too small or underpowered.
- **Sensors**:
  - GPS (navigation)
  - Compass (navigation; don't want to rely on GPS just to get heading)
  - Camera (to detect cones)
  - Distance sensors of some kind (collision avoidance)
  - Lidar (to detect cones; collision avoidance; also just cool)
  - Tactile sensors (to detect contact with cones)
- **Compute**:
  - Something powerful enough to process images from the camera and identify orange cones. I have a Raspberry Pi Model 3 A+ which I'll try out. It may be underpowered (only 512 GB RAM).
  - Planning to base the rest around an RP2040 board, probably one of my Raspberry Pi Picos. Could I just use the more powerful Raspberry Pi computer? Probably, but, among other considerations, I think it's more funny to make the computer be a peripheral for the microcontroller.
- **Dead man's switch**: The Robo-Magellan rules require the operator be able to stop a robot immediately by letting go of a switch. I have a few ideas about this, but nothing definitive. I might use the [RFM69HCW packet radios](https://www.sparkfun.com/products/12775) that I've used before and have a remote send a heartbeat to the robot while a button is pressed, and if that signal doesn't come, a relay cuts off power to the motors. I want to research how other people are doing this and maybe not reinvent the wheel. There's a Sparkfun tutorial called [How to Build a Remote Kill Switch](https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch?_ga=2.46260131.509716641.1684019844-1892652832.1674461773).
- **Logging**: I'll want to log data for later analysis. I got an SD card breakout board for this that I haven't tried out yet.

## Intermediate Milestones

1. **Do a working [TableBot](https://www.hbrobotics.org/index.php/challenges/).** Work on fundamentals in a small form factor. Complete a project of some complexity with CircuitPython. Fun!
1. **Make the remote.** Decide on the dead-man's switch mechanism. Design the PCB for the remote. Get it fabricated. Add panel-mount holes to an enclosure, including a port for the Wii Nunchuck. Attach all the things! Test it with the TableBot.
1. **Get the big DC motors running.** This entails working out all the power management for the motors, and hooking up the motor driver.
1. **Test remote motor power cut-off.** Need to verify this works before getting too far along with everything else.
1. **Figure out how to mount wheels to the big DC motors.** I'm even more of a rookie when it comes to mechanical engineering. Lots to learn here.
1. **Build a chassis.** Figure out how big & what kind of chassis to build. Build it.
1. **Do a working [FloorBot](https://www.hbrobotics.org/index.php/challenges/).** This is another good intermediate goal. I can use the same chassis, motors, remote, etc., but not have to worry about GPS, terrain, and orange cones yet.

## Parts Selection

### Motors

I got four chunky motors at a [Homebrew Robotics Club](hbrobotics.org/) meeting in early 2023. It's been a bit challenging to pin down precisely what they are, but I *think* they are [RAE M1500 permanent magnet DC motors](http://raemotors.com/products/motors/dc-motors/m1500-series/m1500.php) with [G211 right-angle gearmotors](http://raemotors.com/products/motors/gearmotors/right-angle/g211-series.php). Here are the basic specifications. I think they'll do the job.

- Voltage: 18V
- Current: 2A
- Speed: 200 rpm
- Torque: 6 in.-lb.
- Weight: Unknown. Need to weight them. Heavy!

### Battery & Power Distribution

Those motors will need a good amount of power. So far, I think I'll use a small-ish SLA battery. You can get one for about $20. I'll then need to step up the power from 12V to 18V, so I got a [Pololu 4.5-20V Fine-Adjust Step-Up Voltage Regulator U3V70A](https://www.pololu.com/product/2890).

### Chassis

I haven't thought about the chassis much yet. It needs to be able to hold these heavy motors and the SLA battery, which itself is 4.5 pounds.

### Motor Driver

The little motor drivers I've used before won't cut it for driving multiple 18V 2A motors, so I needed to get a beefier driver. I settled on the [Cytron 10A 5-30V Dual Channel DC Motor Driver](https://www.robotshop.com/products/cytron-10a-5-30v-dual-channel-dc-motor-driver?variant=42358540009633). I considered the very cool [RoboClaw](https://www.basicmicro.com/motor-controller) as shown in [Camp Peavy's book *HomeBrewed Robots!*](https://www.amazon.com/HomeBrewed-Robots-Camp-Peavy/dp/B0BW283Q27), but it's expensive and a bit more complex than I need. (I think.)

### Wheels, etc.

I need to figure out how to mount wheels to the motor shafts, which are 1/4" diameter. I don't know much about this part. It seems to be hard to find wheel hubs for 1/4" diameter shafts, but there's probably stuff I'm missing.

### GPS

Thanks to a thread on the [Homebrew Robotics Club mailing list](https://groups.google.com/g/hbrobotics/about), I scored a GPS module for $9. It's the [HiLetgo GY-NEO6MV2](https://www.amazon.com/gp/product/B01D1D0F5M). It's not the best thing ever, but it works, and did I mention that it was $9? It uses a [Ublox NEO-6M](https://www.u-blox.com/en/product/neo-6-series) GPS module. It's 3V compatible and you just communicate to it over a UART. There's a [CircuitPython GPS library](https://docs.circuitpython.org/projects/gps/en/latest/) that works great. It takes several minutes to warm up (or whatever it's doing) but once that's done, it works fine.

### Lidar

I have a [getSurreal XV Lidar Sensor Mount Package](https://www.getsurreal.com/product/xv-lidar-sensor-mount-package/), which uses the lidar sensor from a Neato XV robotic vacuum.

The controller is the [getSurreal Lidar Controller v2.0](https://www.getsurreal.com/product/lidar-controller-v2-0/).

I had to get a replacement [drive belt](https://www.amazon.com/dp/B08KFNRXXV) for the motor that spins the laser around. ($9.95)

### Distance sensors

In addition to the lidar, I'm planning to add a few other distance sensors around the bot for further collision avoidance redundancy, in case something goes wrong with the lidar. I'm not sure yet how many distance sensors I want, or what type to use.

I have a trusty HC-SR04 ultrasonic sensor which uses 5V, as well as a 3.3V equivalent [RCWL-1601](https://www.adafruit.com/product/4007). These will probably work OK, but I'll need to test. I may need to get more depending on what kind of coverage I want.

[My TableBot](https://github.com/anseljh/tablebot) is using some [little infrared sensors](https://www.amazon.com/dp/B07W97H2WS) for detecting the edge of the table, but I doubt they'll be good for this application.

### Compute

I'd like to primarily use a Raspberry Pi Pico. The Pico is a cool little board based on the RP2040 microcontroller chip. I've been programming these in [CircuitPython](https://circuitpython.org/), and it is tons of fun.

There are two tasks that will require more compute power than the little Pico can muster, so I'm planning to use a beefier single-board computer for those tasks, and send their outputs to the Pico. So far I intend to use a Raspberry Pi Model 3 A+. It will process camera images to find the target cones, and send its conclusions to the Pico.

### Logging

I'll log telemetry to a micro SD card. I have a breakout board for that.

Should there be a realtime clock? Might not need one because we can [get time from the GPS](https://docs.circuitpython.org/projects/gps/en/latest/examples.html#time-source).

## Bills of Materials

### Control Board

- [ ] Custom PCB
- [x] Raspberry Pi Pico - $4
- [x] [RFM69HCW packet radio](https://www.sparkfun.com/products/12775) to receive dead-man's switch signal (autonomous mode) and commands from remote (manual mode) - $14
- [x] Antenna - $1
- [x] SMA antenna connector
- [ ] Toggle switch for autonomous/manual mode selection
- [ ] LEDs for autonomous/manual mode indication
- [x] Speaker for auditory output
- [x] GPS module: [HiLetgo GY-NEO6MV2](https://www.amazon.com/gp/product/B01D1D0F5M) - $9
- [x] Magnetometer (compass): [Sparkfun Micromag 3-axis magnetometer](https://www.sparkfun.com/products/retired/244) - $15.49 on eBay
- [x] [Micro SD card breakout board](https://www.adafruit.com/product/4682) for logging - $3.50
- [ ] Bump switch for cone touch detection
- [x] 2x connectors for data from optical encoders (TE Connectivity part no. [3-640442-5](https://www.te.com/usa-en/product-3-640442-5.html?te_bu=Cor&te_type=email&te_campaign=oth_usa_cor-oth-usa-email-ecomm-fy19-hbrs-oconf-prdlink_sma-716_2&elqCampaignId=37418)) - $1.08
- [x] [MCP23008](https://www.adafruit.com/product/593) I2C GPIO expander - $1.95

### Motors and Drive System

- [x] 2x [RAE M1500 permanent magnet DC motors](http://raemotors.com/products/motors/dc-motors/m1500-series/m1500.php) with [G211 right-angle gearmotors](http://raemotors.com/products/motors/gearmotors/right-angle/g211-series.php) - free
- [x] 2x [Broadcom HEDM-5600#J06 optical encoders](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/transmissive-encoders/hedm-5600j06) - *requires 5V* - free
- [x] [Cytron 10A 5-30V Dual Channel DC Motor Driver](https://www.robotshop.com/products/cytron-10a-5-30v-dual-channel-dc-motor-driver?variant=42358540009633) - $23.50

### Power Systems

- [ ] 12V SLA battery, like this [Mighty Max 12V 7 Ah SLA battery](https://www.homedepot.com/p/MIGHTY-MAX-BATTERY-12-Volt-7-Ah-Sealed-Lead-Acid-SLA-Rechargeable-Battery-ML7-12/307979135). It weighs 4.5 pounds. - $20
- [x] [Pololu 4.5-20V Fine-Adjust Step-Up Voltage Regulator U3V70A](https://www.pololu.com/product/2890): I'll use one of these to step up the 12V from the SLA battery to 18V to the motors. ([Bought from RobotShop](https://www.robotshop.com/products/pololu-45-20v-fine-adjust-step-up-voltage-regulator-u3v70a?variant=42360645288097)) - $40.95
- [ ] Fuse holder
- [ ] Fuse (5A?)
- [ ] Big red button for emergency stop
- [ ] Toggle switch for control board power
- [ ] Toggle switch for manual motor power enable/cutoff
- [ ] Relay for motor power control
- [ ] Battery for control board
- [ ] 2x USB to micro-USB cable
  - Battery to Raspberry Pi 3 power
  - Raspberry Pi 3 to lidar controller

### Camera/Lidar System

- [x] Raspberry Pi Model 3 A+ - $25
- [x] Random old webcam (If it doesn't work well enough, get a Raspberry Pi Camera Module)
- [ ] Micro-USB cable from battery
- [x] [getSurreal Lidar Controller v2.0](https://www.getsurreal.com/product/lidar-controller-v2-0/) and [Mount Package](https://www.getsurreal.com/product/xv-lidar-sensor-mount-package/) with Neato XV lidar sensor

### Remote & Dead-Man's Switch

For the safety stop mechanism, I'm envisioning a small handheld device that will double as a remote control when moving the robot manually.

- [ ] Custom PCB
- [x] Raspberry Pi Pico - $4
- [x] [RFM69HCW packet radio](https://www.sparkfun.com/products/12775) - $14
- [x] Antenna - $1
- [x] SMA antenna connector
- [x] [Adafruit Wii Nunchuck Breakout Adapter](https://www.adafruit.com/product/4836) - $2.95
- [x] Wii Nunchuck
- [ ] Big button for dead-man's switch
- [ ] Toggle switch for power
- [ ] Enclosure (I have a few that might work)
- [ ] Green LED for connection indicator
- [ ] Red LED for heartbeat blink
- [ ] Another LED for mode indicator?

## Pins Required

### Control Pico

- 2 for UART to Pi 3
- 2 for UART to GPS module
- SPI (4) + 1 = **5** for radio
- SPI (3 reused + 1 CS) + 2 = **3** for magnetometer
- SPI (reuse 3 + 1 CS) + 1 = **2** for [Adafruit Micro SD SPI or SDIO Card Breakout](https://www.adafruit.com/product/4682)
- 2x2 = **4** for optical encoders
- 1 for mode selection switch
- 1 for mode selection LED
- 1 for speaker
- 1 for bump switch
- 1 for motor power relay
- 4 for motor driver

Total: **27**

Uh-oh; there are only 26 usable GPIO pins on the Pico. We'll have to offload some of this to an IO expander. I have both an [MCP23008](https://www.adafruit.com/product/593) and an [MCP23017](https://www.adafruit.com/product/732) for that (I2C to 8 or 16 GPIO, respectively).

### Raspberry Pi 3

- 2 for UART to Pico

Total: **2**

### Remote Pico

- 1 for dead-man's switch
- 5 for radio
- 2 for I2C to Nunchuck breakout board
- 3 for indicator LEDs

Total: **11**
