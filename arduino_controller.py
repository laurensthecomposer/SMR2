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

        self.belts = [Belts( self, 'm', 'n', 'o' ),
                      Belts( self, 'r', 's', 't' ),
                      Belts( self, 'u', 'v', 'w' )]
    def all_forward(self):
        for belt in self.belts:
            belt.forward()

    def all_stop(self):
        for belt in self.belts:
            belt.stop()

    def all_backwards(self):
        for belt in self.belts:
            belt.backwards()

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

    @property
    def gate_state(self):
        self.connection.write(b'l')
        self.connection.flush()
        arduinoData = int(self.connection.readline().decode('ascii'))
        if arduinoData == 1: # broken
            return True
        elif arduinoData == 2: # unbroken
            return False


class Belts( object ):
    def __init__(self, connection: Arduino,  forward_letter : str, stop_letter: str, reverse_letter: str ):
        self.f = bytes(forward_letter, 'utf-8')
        self.s = bytes(stop_letter, 'utf-8')
        self.r = bytes(reverse_letter, 'utf-8')
        self.arduino: Arduino = connection

    def first_forward(self):
        self.arduino.connection.write( self.m)
        self.arduino.connection.flush()
        arduinoData = self.arduino.connection.readline().decode('ascii')

    def first_stop(self):
        self.arduino.connection.write(self.n)
        self.arduino.connection.flush()
        arduinoData = self.arduino.connection.readline().decode('ascii')

    def first_backwards(self):
        self.arduino.connection.write( self.o )
        self.arduino.connection.flush()
        arduinoData = self.arduino.connection.readline().decode('ascii')

