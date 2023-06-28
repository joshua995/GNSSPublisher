# GNSSPublisher
For this program to run you will need to have the GNSS unit connected, and 
in your terminal you have to run: sudo chmod 666 /dev/ttyACM0 

to allow permission to access the serial port.
/dev/ttyACM0 is a default for serial data so it should all be the same on linux.

You should be able to create a subscriber program to access the data similar to the listener.py program.

Basic steps to run the GNSSPublisher.py
1. Pull this src folder by running this in your terminal: git clone https//github.com/joshua995/GNSSPublisher.git
2. Drag the GNSSPublisher folder from your home directory in your catkin workspace's src folder
3. In your catkin workspace directory run catkin_make
4. Plug in the GNSS unit
5. After the setup to allow ROS programs to work, run the GNSS publisher program with:
     source devel/setup.bash
     rosrun gnss GNSSPublisher.py

You should now see the latitude and longitude being printed on the terminal.

In another terminal if you run : 
  source devel/setup.bash
  rosrun gnss listener.py

The subscriber will print out its own message along with the lat,lon from the GNSSPublisher.py

At competition, the GNSSPublisher.py can publish the speed in knots & Km/h, the altitude, and can be run through a launch file with the other programs.
