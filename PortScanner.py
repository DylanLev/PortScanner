#!/usr/bin/python3

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

# host = "137.74.187.100"
host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("the port is closed")
    else:
        print("The port is open")

portScanner(port)