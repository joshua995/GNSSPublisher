# Joshua Liu
# 2023-06-27
# This is a publisher of the GNSS data using the serial port.
# The data can be accessed via subscribing to it.
# Set GNSS unit to 10Hz using U-Center
# Sentences that are currently not in use are:
# GLL: does not work at 10Hz

import rospy
from std_msgs.msg import String
import serial

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1000)

    fileNameLatLon = "Coordinates.txt"
    fileNameKnotsKmHAlt = "SpeedsAlt.txt"
    
    serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=38400, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    
    ggaLat, ggaLon, ggaAlt = 0, 0, 0
    rmcLat, rmcLon, rmcKnots = 0, 0, 0
    vtgKnots, vtgKmH = 0, 0

    averageLat, averageLon = [], []
    
    while not rospy.is_shutdown():
        if serialPort.in_waiting:
            serialString = serialPort.readline()
            splitSerialString = serialString.decode('Ascii').split(",")
            if serialString.__contains__(bytes("RMC", "utf-8")):
                rmcLat, rmcLon, rmcKnots = splitSerialString[3], splitSerialString[5], splitSerialString[7]
            if serialString.__contains__(bytes("VTG", "utf-8")):
                vtgKnots, vtgKmH = splitSerialString[5], splitSerialString[7]
            if serialString.__contains__(bytes("GGA", "utf-8")):
                ggaLat, ggaLon, ggaAlt = splitSerialString[2], splitSerialString[4], splitSerialString[9]

                if ggaLat != "" and rmcLat != "":
                    averageLat = (float(ggaLat) + float(rmcLat)) / 2
                    averageLon = (float(ggaLon) + float(rmcLon)) / 2
                    
                    latLonString = " " + str(averageLat) + "," + str(averageLon)
                    speedsAltString = " " + str((float(vtgKnots) + float(rmcKnots)) / 2) + "," + str(vtgKmH) + "," + str(ggaAlt)

                    with open(fileNameLatLon, "a") as coordFile:
                        coordFile.write(latLonString)

                    with open(fileNameKnotsKmHAlt, "a") as saFile:
                        saFile.write(speedsAltString)
                    rospy.loginfo(latLonString)
                    pub.publish(latLonString)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
