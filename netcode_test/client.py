import socket
import netcode

netcode.DEFAULT_TIMEOUT = 25.0

ip_addr = input("Give IP of server: ")
port_num = input("give port number: ")

Cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Cs.connect((ip_addr, int(port_num)))
netcode.configure_socket(Cs)

buffersize = 10

while True:
    data_pack = netcode.recieve_data(Cs,buffersize)
    data = data_pack[0]

    connected = data_pack[3]
    if(connected == False):
        break

    print(data)

    send_data = input("give some data to be sent: ")
    send_data = eval(send_data)
    connected = netcode.send_data(Cs,buffersize,send_data)

    if(connected == False):
        break
