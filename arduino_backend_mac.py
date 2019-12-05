import serial

ser = serial.Serial(port='/dev/cu.usbmodem14101', baudrate = 9600, timeout=1)

#def sendInst():


while(1):

    userInput = input('Send instruction?')

    if userInput == 'l':
        ser.write(b'l')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 'r':
        ser.write(b'r')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 's':
        ser.write(b's')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)


