import socket
import netcode

netcode.DEFAULT_TIMEOUT = 25.0

HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)

print("IP: " + str(IP))

PORT = int(input("Please give port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen()

Cs, Caddress = s.accept()
netcode.configure_socket(Cs)

buffersize = 10

while True:
    send_data = input("give some data to be sent: ")
    send_data = eval(send_data)
    connected = netcode.send_data(Cs,buffersize,send_data)

    if(connected == False):
        break

    data_pack = netcode.recieve_data(Cs,buffersize)
    data = data_pack[0]

    connected = data_pack[3]
    if(connected == False):
        break

    print(data)
