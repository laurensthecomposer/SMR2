import serial

macport = '/dev/cu.usbmodem14101'
ser = serial.Serial(port= macport, baudrate = 9600, timeout=1)

while True:

    userInput = input('Send instruction?')

    if userInput == 'l':  # get lightgate status
        ser.write(b'l')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 'm':  # forward motor
        ser.write(b'm')

        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 'n':  # stop motor
        ser.write(b'n')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 'o':  # reverse motor
        ser.write(b'o')
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)

    if userInput == 'r':  # forward motor
            ser.write(b'r')
            arduinoData = ser.readline().decode('ascii')
            print(arduinoData)

    if userInput == 's':  # stop motor
            ser.write(b's')
            arduinoData = ser.readline().decode('ascii')
            print(arduinoData)

    if userInput == 't':  # reverse motor
            ser.write(b't')
            arduinoData = ser.readline().decode('ascii')
            print(arduinoData)

    if userInput == 'u':  # forward motor
                ser.write(b'u')
                arduinoData = ser.readline().decode('ascii')
                print(arduinoData)

    if userInput == 'v':  # stop motor
                ser.write(b'v')
                arduinoData = ser.readline().decode('ascii')
                print(arduinoData)

    if userInput == 'w':  # reverse motoru

                ser.write(b'w')
                arduinoData = ser.readline().decode('ascii')
                print(arduinoData)

    if userInput == 'a':  # reverse motoru

                ser.write(b'a')
                arduinoData = ser.readline().decode('ascii')
                print(arduinoData)


    if userInput == 'q':  # reverse motoru


                ser.write(b'q')
                arduinoData = ser.readline().decode('ascii')
                print(arduinoData)
