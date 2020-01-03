import serial
import discord
import asyncio

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    cc = ser.readline().decode()
    print(cc)
