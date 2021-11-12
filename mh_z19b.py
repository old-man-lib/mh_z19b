import serial
import binascii

def read():
	ser = serial.Serial('/dev/serial0', 9600, timeout=1)
	query = bytearray(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')
	ser.write(query)
	answer = ser.read(9)
	ser.close()
	bytes = bytearray(answer)
	return (bytes[2]*256 + bytes[3])
#print(bytes[2]*256 + bytes[3])

