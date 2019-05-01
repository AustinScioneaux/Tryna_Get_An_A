from Tkinter import *

class MainGui(Frame):
        def __init__(self, parent):
                Frame.__init__(self, parent)
                self.pack()                

        def MainMenu(self):
                
                mainFrame= Frame(self, height=HEIGHT, width = WIDTH)
                MainGui.start = Button(mainFrame, command=lambda: g.testButton("start button pressed"), fg= "white", bg ="blue", text = "Start Game")
                MainGui.start.grid(row=0, column= 0)

                mainFrame.pack()
                
        def testButton(self, text):
                print text
                
######################################################################################
WIDTH = 800
HEIGHT = 480

####################################################################################

window = Tk()
window.title("Lancers")

g = MainGui(window)

g.MainMenu()
window.mainloop()
