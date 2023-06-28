# Joshua Liu
# 2023-06-27
# This is a publisher of the GNSS data using the serial port.
# The data can be accessed via subscribing to it.
import rospy
from std_msgs.msg import String
import serial

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=38400, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    
    ggaLat, ggaLon, ggaAlt = 0, 0, 0
    rmcLat, rmcLon = 0, 0
    gllLat, gllLon = 0, 0

    averageLat, averageLon = [], []
    
    while not rospy.is_shutdown():
        if serialPort.in_waiting:
            serialString = serialPort.readline()
            splitSerialString = serialString.decode('Ascii').split(",")
            if serialString.__contains__(bytes("GGA", "utf-8")):
                ggaLat, ggaLon, ggaAlt = splitSerialString[2], splitSerialString[4], splitSerialString[9]
            if serialString.__contains__(bytes("RMC", "utf-8")):
                rmcLat, rmcLon = splitSerialString[3], splitSerialString[5]
            if serialString.__contains__(bytes("GLL", "utf-8")):
                gllLat, gllLon = splitSerialString[1], splitSerialString[3]
                averageLat = (float(ggaLat) + float(gllLat) + float(rmcLat)) / 3
                averageLon = (float(ggaLon) + float(gllLon) + float(rmcLon)) / 3
                latLonString = " " + str(averageLat) + "," + str(averageLon)
                rospy.loginfo(latLonString)
                pub.publish(latLonString)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
