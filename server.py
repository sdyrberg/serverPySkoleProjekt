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

            list1 = l[2:6]

            list2 = l[6:10]

            list3 = l[10:14]

            list4 = l[14:18]

            list5 = l[18:22]

            list6 = l[22:26]

            list7 = l[26:30]

            list8 = l[30:34]

            list9 = l[34:38]

            sqlFormula = "INSERT INTO " + bordnummer + " (Bestilt, Antal, Størrelse, Ordrenummer, Ekstra) VALUES (%s, %s, %s, %s, %s)"
            if len(list1[0]) != 0:
                list1.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list1)
                print(list1)

            if len(list2[0]) != 0:
                list2.append(newOrdreNummer)
                mycursor.execute(sqlFormula, list2)
                print(list2)

                if len(list3[0]) != 0:
                    list3.append(newOrdreNummer)
                    mycursor.execute(sqlFormula, list3)
                    print("list3 sendt")

                if len(list4[0]) != 0:
                    list4.append(newOrdreNummer)
                    mycursor.execute(sqlFormula, list4)
                    print("list4 sendt")

                if len(list5[0]) != 0:
                    list5.append(newOrdreNummer)
                    mycursor.execute(sqlFormula, list5)
                    print("list5 sendt")

                if len(list6[0]) != 0:
                    list6.append(newOrdreNummer)
                    mycursor.execute(sqlFormula, list6)
                    print("list6 sendt")

                if len(list7[0]) != 0:
                    list7.append(newOrdreNummer)
                    mycursor.execute(sqlFormula, list7)
                    print("list7 sendt")

                if len(list8[0]) != 0:
                    list8.append(newOrdreNummer)
                    mycursor.execute(sqlFormula, list8)
                    print("list8 sendt")

                if len(list9[0]) != 0:
                    list9.append(newOrdreNummer)
                    mycursor.execute(sqlFormula, list9)
                    print("list9 sendt")

            mydb.commit()

serversocket.listen(5)
print('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
