##"server.py" - Quick netcode.py test (server code)
##Copyright (C) 2022  Lincoln V.
##
##This program is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License
##along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
