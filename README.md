# GNSSPublisher
There are 3 files you can run after you clone this repository:
1. GNSSPublisher.py
2. GNSSPublisherFileLog.py
3. listener.py
   
The current version can run when the unit is updating at a frequency of 1Hz or 10Hz (Current).
The GLL sentence is omitted, because it does not update properly at 10Hz.

Setting up the code (Linux-ROS):
1. Run the following in the terminal to clone this repository:
   
   git clone https//github.com/joshua995/GNSSPublisher.git
3. From your file directory, drag the cloned repository (GNSSPublisher folder) to your src folder in the catkin workspace you are using.
4. Run the following in the terminal to allow serial communication in python:
   
   pip install pyserial
6. Navigate to your catkin workspace directory from the terminal, and run:
   
   catkin_make
   
Setting up the GNSS unit to work with the code:
1. Plug in the GNSS to your computer.
2. If you are using a VM, allow the connection to "u-blox AG ..." usb devices.
3. From the root directory in the terminal run:
  
   sudo cat /dev/ttyACM0 
   If no warnings appear and GNSS sentences are not printing on the terminal, you have to replace /dev/ttyACM0 to the port that will print out the sentences (The port the device is connected to). If a warning appears that tells you the directory does not exist, then the unit is not connected to that port.
4. To allow serial communcation to the serial port after the unit is connected, run:
  
   sudo chmod 666 /dev/ttyACM0
If the unit is connected properly, running "sudo cat /dev/ttyACM0" in the root directory will print out the GNSS sentences.
Running the program:
Open 3 terminals
In the first terminal run: roscore
In the second terminal:
Navigate to your catkin workspace.
Run: source devel/setup.bash
Run: rosrun gnss GNSSPublisher.py
At this point, the terminal should print out the latitude and longitude in this format: lat,lon
In the third terminal:
Navigate to your catkin workspace.
Run: source devel/setup.bash
Run: rosrun gnss listener.py
At this point, the terminal should print out the latitude and longitude in this format: I have received the published lat/lon lat,lon

Now the publisher (GNSSPublisher.py) is printing the lat/lon from the GNSS unit, and the subscriber (listener.py) is printing the lat/lon from the GNSSPublisher.py program.

GNSSPublisherFileLog.py: In addition to publishing the same lat/lon to subscribers as the GNSSPublisher.py, it will log the latitude, longitude, speed in knots, speed in km/h and the altitude in a txt file for post analysis or use during the task at hand. To run this, replace the step "3b Run: rosrun gnss GNSSPublisher.py" with: rosrun gnss GNSSPublisherFileLog.py


