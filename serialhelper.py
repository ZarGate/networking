import time
import serial
import sys


class Serialhelper:
    ser = None
    out = ''

    def __init__(self):
        port = raw_input('Serial interface: ')
        self.ser = serial.Serial(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        self.ser.isOpen()
        self.write('')
        self.write('')
        self.write('')
        self.write('')
        self.write('')
        self.write('')
        self.write('')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.ser.close()

    def write(self, data):
        self.ser.write(data + '\n')

    def writeread(self, data):
        self.ser.write(data + '\n')
        time.sleep(0.5)
        out = ''
        while self.ser.inWaiting() > 0:
            read = self.ser.read(1)
            self.out += read
            out += read
            sys.stdout.write(read)
        return out


    def flush(self):
        self.out = ''

    def readtoinfinity(self, waitfor=None):
        time.sleep(1)
        while True:
            if self.ser.inWaiting() > 0:
                read = self.ser.read(1)
                self.out += read
                sys.stdout.write(read)
            if waitfor and waitfor in self.out[-500:]:
                return
