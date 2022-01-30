from socket import *
import time

UDP_Port_Number = 12000
UDP_IP_Address = "127.0.0.1"

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set a timeout value of 1 second for the created socket
clientSocket.settimeout(1)
ping_number = 1
while ping_number <= 10:
    start_time = time.time()
    try:
        message = 'Ping ' + str(ping_number) + " " + str(time.strftime("%H:%M:%S"))
        clientSocket.sendto(bytes(message.encode()), (UDP_IP_Address, UDP_Port_Number))
        print("Send to message : " + message)
        data, server = clientSocket.recvfrom(1024)
        finish_time = time.time()
        rtt = finish_time - start_time
        print("Respond : ", data.decode(), " Round Trip Time(RTT): ", rtt)
    except timeout:
        print('REQUEST TIMED OUT')
    ping_number += 1
    if ping_number > 10:
        clientSocket.close()
