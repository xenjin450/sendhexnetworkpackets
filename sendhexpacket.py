#Libraries
import socket 
import sys 

#Target IP/Port
HOST = input("Target Host/IP:")
PORT = int(input("Target Port:"))
#hexdata to send 
hexdata = ''
#Encoding Hex Data To Bytes 
hexpacket = bytes.fromhex(hexdata)
#Socket Configuration
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect To Traget IP/Port
s.connect((HOST,PORT))
#Send The Final Hex Packet
s.send(hexpacket)
