from Tkinter import *
from Player import *
from time import sleep

redLed = 18
redLed2 = 19
yellowLed = 20
greenLed = 21

GPIO.setup(redLed, GPIO.OUT, initial=0)
GPIO.setup(redLed2, GPIO.OUT, initial = 0)
GPIO.setup(yellowLed, GPIO.OUT, initial = 0)
GPIO.setup(greenLed, GPIO.OUT, initial = 0)

class MainGui(Frame):
        def __init__(self, parent):
                self.parent = parent
                self.networking= 0
                self.running = False
                self.p1 = Player(17,16)
                self.p2 = Player(13, 12)

                #set some defailt controls for p2
                self.p2.controls.forward = "w"
                self.p2.controls.backward="s"
                self.p2.controls.leftTurn = "a"
                self.p2.controls.rightTurn= "d"

                Frame.__init__(self, parent)
                self.pack()                

        def mainMenu(self, frameToForget = None):
                buttonWidth = 8
                buttonHeight = 2
                #nothing to forget- you need to build everything
                if(frameToForget == None):
                        pass
                else:
                        frameToForget.pack_forget()

                mainFrame= Frame(self.parent, height=HEIGHT, width = WIDTH, background="red")
                
                #background image
                fileName = PhotoImage(file = "mainMenu.gif")
                background_label = Label(mainFrame, image=fileName)
                background_label.image=fileName
                background_label.place(x=0, y=0)

                start = Button(mainFrame, command = lambda: self.battle(mainFrame), fg = "white", bg ="blue", text = "Start Game", font = "Verdana 16 bold",height= buttonHeight, width = buttonWidth)
                start.pack(side = TOP, expand = 1)

                options = Button(mainFrame, command = lambda: self.settings(mainFrame), fg = "white", bg = "blue", text = "Options", font = "Verdana 16 bold", height= buttonHeight, width = buttonWidth)
                options.pack(side = TOP, expand = 1)

                linkpi = Button(mainFrame, command = lambda: self.testButton("Link pi button pressed"), fg = "white", bg = "blue", text = "LINK PI", font = "Verdana 16 bold", height= buttonHeight, width = buttonWidth)
                linkpi.pack(side = TOP, expand = 1)

                #exit
                exitGame = Button(mainFrame, command = lambda: self.exitGame(), fg = "white", bg = "blue", text = "Exit Game", font= "Verdana 16 bold", height= buttonHeight, width = buttonWidth)
                exitGame.pack(side = TOP, expand =1)
                
                mainFrame.pack_propagate(0)
                mainFrame.pack()

                
                
                

        def settings(self, frameToForget):
                #forget last frame
                frameToForget.pack_forget()
                
                networkingStr=["No", "Yes"]
                ctrlButtons = {}
                ctrlButtons2 = {}

                buttonWidth = 8
                buttonHeight = 2

                #typical color scheme for labels
                labelfg= "white"
                labelbg = "green"

                settingsFrame = Frame(self.parent, height = HEIGHT, width = WIDTH, background = "yellow")

                 #background image
                fileName = PhotoImage(file = "options.gif")
                background_label = Label(settingsFrame, image=fileName)
                background_label.image=fileName
                background_label.place(x=0, y=0)

                #back button
                back = Button(settingsFrame, text = "Back", command = lambda: self.mainMenu(settingsFrame), fg = "black", bg = "blue", font = "Verdana 16 bold", height = 1, width = 2)
                back.place(x=0, y =0)

                #Two or 1 pi setting
                networkOption = Label(settingsFrame, text = "Two Pis", fg = "blue", bg = "white", font = "Verdana 16 bold", height = buttonHeight, width = buttonWidth)
                networkOption.grid(row = 0, column = 1, rowspan = 1, columnspan = 2, sticky= N+S+W+E)
                
                networkButton = Button(settingsFrame, command = lambda: self.changeNetwork(networkButton, networkingStr, p2Frame), fg = "white", bg = "blue", text = networkingStr[self.networking], font = "Verdana 16 bold", height = buttonHeight, width = buttonWidth) 
                networkButton.grid(row = 0, column = 3, rowspan = 1, columnspan = 2, sticky= N+S+W+E)

                #controls
                ctrlTitle = Label(settingsFrame, text = "Controls For P1", fg = "blue", bg = "red", font = "Verdana 24 bold", padx=10)
                ctrlTitle.grid(row = 1, column = 1, rowspan = 1, columnspan = 4, sticky = N+S)

                #Forward ctrl part
                forward = Label(settingsFrame, text = "Forward-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                forward.grid(row = 2, column = 1, rowspan = 1, columnspan = 1, sticky = W+E+N+S)
                
                ctrlForward = Button(settingsFrame, text=self.p1.controls.forward, command = lambda: self.changeControl(ctrlButtons, self.p1), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlForward.grid(row = 2,column=2,padx = (0,25), sticky = W+E+N+S)
                ctrlButtons["ctrlForward"] = ctrlForward
                
                #Backward ctrl part
                backward = Label(settingsFrame, text = "Backward-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                backward.grid(row = 2, column = 3, rowspan = 1, columnspan = 1, sticky = W+E+N+S) 

                ctrlBackward = Button(settingsFrame, text = self.p1.controls.backward, command = lambda: self.changeControl(ctrlButtons, self.p1), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlBackward.grid(row = 2,column=4, sticky = W+E+N+S)
                ctrlButtons["ctrlBackward"] = ctrlBackward
                #Left turn ctr part
                left = Label(settingsFrame, text = "Turn Left-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                left.grid(row = 3, column = 1, rowspan = 1, columnspan = 1, sticky = W+E+N+S) 

                ctrlLeft = Button(settingsFrame, text = self.p1.controls.leftTurn, command = lambda: self.changeControl(ctrlButtons, self.p1), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlLeft.grid(row = 3,column=2,padx = (0,25), sticky = W+E+N+S)
                ctrlButtons["ctrlLeft"] = ctrlLeft
                
                #Right turn ctrl part
                right = Label(settingsFrame, text = "Turn Right-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                right.grid(row = 3, column = 3, rowspan = 1, columnspan = 1, sticky = W+E+N+S) 

                ctrlRight = Button(settingsFrame, text = self.p1.controls.rightTurn, command = lambda: self.changeControl(ctrlButtons, self.p1), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlRight.grid(row = 3,column=4, sticky = W+E+N+S)
                ctrlButtons["ctrlRight"] = ctrlRight

                ####################################################################
                # 2nd player part
                ####################################################################

                p2Frame = Frame(settingsFrame)
                p2Frame.grid(row = 4, column = 1, rowspan = 3, columnspan = 4)

                #background image
                fileName = PhotoImage(file = "options.gif")
                background_label = Label(p2Frame, image=fileName)
                background_label.image=fileName
                background_label.place(x=-120, y=-187)
                
                #Helps with spacing
                p2Frame.grid_rowconfigure(1, minsize= 45)
                p2Frame.grid_columnconfigure(1, minsize=150)
                p2Frame.grid_columnconfigure(3, minsize=150)
                
                #controls title 2
                ctrlTitle2 = Label(p2Frame, text = "Controls For P2", fg = "blue", bg = "red", font = "Verdana 24 bold", padx=10)
                ctrlTitle2.grid(row = 0, column = 0, rowspan = 1, columnspan = 4, sticky = N+S)

                #Forward ctrl part 2
                forward2 = Label(p2Frame, text = "Forward-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                forward2.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, sticky = W+E+N+S)
                
                ctrlForward2 = Button(p2Frame, text=self.p2.controls.forward, command = lambda: self.changeControl(ctrlButtons2, self.p2), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlForward2.grid(row = 1,column=1,padx = (0,25), sticky = W+E+N+S)
                ctrlButtons2["ctrlForward"] = ctrlForward
                
                #Backward ctrl part 2
                backward2 = Label(p2Frame, text = "Backward-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                backward2.grid(row = 1, column = 2, rowspan = 1, columnspan = 1, sticky = W+E+N+S) 

                ctrlBackward2 = Button(p2Frame, text = self.p2.controls.backward, command = lambda: self.changeControl(ctrlButtons2, self.p2), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlBackward2.grid(row = 1,column=3, sticky = W+E+N+S)
                ctrlButtons2["ctrlBackward"] = ctrlBackward
                
                #Left turn ctr part 2
                left2 = Label(p2Frame, text = "Turn Left-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                left2.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, sticky = W+E+N+S) 

                ctrlLeft2 = Button(p2Frame, text = self.p2.controls.leftTurn, command = lambda: self.changeControl(ctrlButtons2, self.p2), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlLeft2.grid(row = 2,column=1,padx = (0,25), sticky = W+E+N+S)
                ctrlButtons2["ctrlLeft"] = ctrlLeft
                
                #Right turn ctrl part 2
                right2 = Label(p2Frame, text = "Turn Right-", fg = labelfg, bg = labelbg, font = "Verdana 16 bold")
                right2.grid(row = 2, column = 2, rowspan = 1, columnspan = 1, sticky = W+E+N+S) 

                ctrlRight2 = Button(p2Frame, text = self.p2.controls.rightTurn, command = lambda: self.changeControl(ctrlButtons2, self.p2), fg ="white", bg = "blue",  font = "Verdana 16 bold")
                ctrlRight2.grid(row = 2, column = 3, sticky = W+E+N+S)
                ctrlButtons2["ctrlRight"] = ctrlRight
                
                #maintain a certain size with widgets in these locations
                settingsFrame.grid_rowconfigure(1, minsize= 45)
                settingsFrame.grid_columnconfigure(2, minsize=150)
                settingsFrame.grid_columnconfigure(4, minsize=150)

                #this is used to center widgets
                settingsFrame.grid_columnconfigure(0, weight=1)
                settingsFrame.grid_columnconfigure(5, weight=1)

                #Stops gui from resizing frame
                settingsFrame.grid_propagate(0)
                settingsFrame.pack()

        def testButton(self, text):
                print text
                
        def exitGame(self):
                GPIO.cleanup()
                window.destroy()

        def changeNetwork(self, button, string, frame):
                if (self.networking == 1):
                        self.networking = 0
                        frame.grid(row = 4, column = 1, rowspan = 3, columnspan = 4)
                        
                elif(self.networking == 0):
                        self.networking = 1
                        frame.grid_forget()
                
                button.config(text = string[self.networking])
                
                
        def changeControl(self, ctrlButtons, player):
                #need to update button text instantly
                key = read_key()

                #change button text and 
                if (ctrlButtons["ctrlForward"]["state"]==ACTIVE):
                        player.controls.forward= key
                        ctrlButtons["ctrlForward"].config(text = player.controls.forward)
                elif(ctrlButtons["ctrlBackward"]["state"]==ACTIVE):
                        player.controls.backward=key
                        ctrlButtons["ctrlBackward"].config(text = player.controls.backward)
                elif(ctrlButtons["ctrlLeft"]["state"]==ACTIVE):
                        player.controls.leftTurn=key
                        ctrlButtons["ctrlLeft"].config(text = player.controls.leftTurn)
                elif(ctrlButtons["ctrlRight"]["state"]==ACTIVE):
                        player.controls.rightTurn=key
                        ctrlButtons["ctrlRight"].config(text = player.controls.rightTurn)

        def battle(self, frameToForget):
                #frameToForget.pack_forget()
                frameToForget.pack_forget()
                
                self.p1.robot.startPins()
                self.p2.robot.startPins()

                #Build frame part
                battleFrame = Frame(self.parent, height = HEIGHT, width = WIDTH, background = "red")
                battleFrame.pack_propagate(0)
                battleFrame.pack()

                

                #3
                GPIO.output(redLed, 1)

                number = Label(battleFrame, text = "3", fg = "white", bg = "red4", font = "Verdana 150 bold")
                number.pack(side = TOP, expand = 1, fill = BOTH)
                window.update()

                sleep(1)
                GPIO.output(redLed, 0)
                

                #2
                GPIO.output(redLed2, 1)
                
                number.config(bg = "red", text = "2")
                window.update()

                sleep(1)
                GPIO.output(redLed2, 0)

                #1
                GPIO.output(yellowLed, 1)
                
                number.config(bg="yellow", text = "1")
                window.update()

                sleep(1)
                GPIO.output(yellowLed, 0)
                GPIO.output(greenLed, 1)

                #battle screen
                fileName = PhotoImage(file = "battle.gif")
                background_label = Label(battleFrame, image=fileName)
                background_label.image=fileName
                background_label.place(x=0, y=0)
                window.update()
                
                var = 0
                #infinite loop
                while(True):
                        window.update()
                        self.p1.runSchem1()
                        self.p2.runSchem1()
                        if(is_pressed("1")):
                                var = 1
                                break
                        elif(is_pressed("2")):
                                var = 2
                                break

                GPIO.output(greenLed, 0)
                if(var == 1):
                        self.victory(battleFrame, var)
                elif(var == 2):
                        self.victory(battleFrame, var)

        def victory(self, frameToForget, var):
                buttonWidth = 8
                buttonHeight = 2
                
                frameToForget.pack_forget()
                
                victoryFrame = Frame(self.parent, height = HEIGHT, width = WIDTH, background = "red")
                victoryFrame.pack_propagate(0)
                victoryFrame.pack()
                
                if(var == 1):
                        fileName = PhotoImage(file = "p1victoryScreen.gif")
                elif(var == 2):
                        fileName = PhotoImage(file = "p2victoryScreen.gif")
                
                background_label = Label(victoryFrame, image=fileName)
                background_label.image=fileName
                background_label.place(x=0, y=0)
               
                

                exitButton = Button(victoryFrame, command = lambda: self.exitGame(), fg = "white", bg ="blue", text = "Exit", font = "Verdana 16 bold",height= buttonHeight, width = buttonWidth)
                exitButton.pack(side = BOTTOM)
                
                
                mainButton = Button(victoryFrame, command = lambda: self.mainMenu(victoryFrame), fg = "white", bg ="blue", text = "MainMenu", font = "Verdana 16 bold",height= buttonHeight, width = buttonWidth)
                mainButton.pack(side = BOTTOM)

                
                
######################################################################################
WIDTH = 800
HEIGHT = 480

####################################################################################


window = Tk()
window.title("Lancers")

g = MainGui(window)

g.mainMenu()



window.mainloop()
