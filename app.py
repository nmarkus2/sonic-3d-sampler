import serial

print("printing the incoming data below....")
ser = serial.Serial(port='/dev/tty.usbserial-1420',baudrate=57600,bytesize=8,stopbits=1)
ser.flushInput()
while True:
    try:
        ser_bytes = ser.readline()
        text = str(ser_bytes,'utf-8').strip()
        wx =  text.split(";")[1]
        wy = text.split(";")[2]
        wz = text.split(";")[3]
        temp1 = text.split(";")[4]
        print("Wx=",wx,"Wy=",wy,"Wz=",wz,"Temp=",temp1)
        #print("Wx=", wx,"Wy=", wy,"Wz=", wz,"Temp=", temp)
       
    except:
        print("keyboard interrupt")
        break
