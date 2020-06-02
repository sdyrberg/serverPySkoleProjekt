import socket
import VolControl

from threading import *

import mysql.connector

mydb = mysql.connector.connect(user="Søren",
                               passwd="1234",
                               host="localhost",
                               database="testdb")
mycursor = mydb.cursor()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.189"
port = 8000
print(host)
print(port)
serversocket.bind((host, port))


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:

            data = self.sock.recv(1024).decode()
            l = data.split("-")
            print(l)
            if data:
                fin = open("OrdreNummer.txt", "rt")
                ordrenummer = fin.read()
                newOrdreNummer = int(ordrenummer) + 1
                fin.close()
                fin = open("OrdreNummer.txt", "wt")
                fin.write("")
                fin.write(str(newOrdreNummer))
                fin.close()
                print(newOrdreNummer)
            bordnummer = l[1]
            menuVælger = l[0]

            list1 = l[2:5]

            list2 = l[5:8]

            list3 = l[8:11]

            list4 = l[11:14]

            list5 = l[14:17]

            list6 = l[17:20]

            list7 = l[20:23]

            list8 = l[23:26]

            list9 = l[26:29]

            sqlFormula = "INSERT INTO " + bordnummer + " (Bestilt, Antal, Størrelse, Ordrenummer) VALUES (%s, %s, %s, %s)"

            if list1:
                list1.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list1)

            if list2:
                list2.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list2)
                print("OK")
            if list3:
                list3.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list3)

            if list4:
                list4.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list4)

            if list5:
                list5.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list5)

            if list6:
                mycursor.execute(sqlFormula, list6)
                list6.append(newOrdreNummer)
            if list7:
                list7.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list7)
            if list8:
                list8.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list8)
            if list9:
                list9.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list9)

            mydb.commit()

            if data == "+":
                print("Vol UP")
                VolControl.volUp()

            if data == "-":
                print("Vol Down")
                VolControl.volDown()


serversocket.listen(5)
print('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
