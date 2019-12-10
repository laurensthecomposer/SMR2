import serial

ser = serial.Serial(port='COM5', baudrate = 9600, timeout=1)

while True:

    userInput = input('Send instruction?')

    if userInput == 'l':  # get lightgate status
        ser.write(b'l')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 'f':  # forward motor
        ser.write(b'f')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 's':  # stop motor
        ser.write(b's')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 'r':  # reverse motor
        ser.write(b'r')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)
