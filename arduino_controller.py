import serial
import serial.tools.list_ports
import time


class Arduino( object ):
    def __init__(self, com=None, baud=9600):
        self.baud = baud
        self._connected = False
        if com == None:
            self.auto_connect()
        else:
            self.port = com
            self.connect()

    def connect(self):
        # Declare the port and baudrate for the Arduino
        self.connection = serial.Serial( self.port, self.baud, timeout=1 )
        time.sleep( 2 )
        self._connected = True
        return self.connected

    def auto_connect(self):
        port_list = self.list_ports()
        self.port = port_list[0].device
        self.connect()

    @staticmethod
    def list_ports():
        ports = list( serial.tools.list_ports.comports() )
        return ports

    @property
    def connected(self):
        return self._connected

    def backwards(self):
        self.connection.write( b'r' )
        self.connection.flush()
        arduinoData = self.connection.readline().decode('ascii')

    def forward(self):
        self.connection.write( b'f' )
        self.connection.flush()
        arduinoData = self.connection.readline().decode('ascii')

    def stop(self):
        self.connection.write(b's')
        self.connection.flush()
        arduinoData = self.connection.readline().decode('ascii')

    @property
    def gate_state(self):
        self.connection.write(b'l')
        self.connection.flush()
        arduinoData = int(self.connection.readline().decode('ascii'))
        if arduinoData == 1: # broken
            return True
        elif arduinoData == 2: # unbroken
            return False


