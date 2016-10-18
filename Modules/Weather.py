from tkinter import *
import Helpers.Modules.Weather.WeatherInformation as WI

class Application(Frame):

    weatherinfo = WI.WeatherInfo()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Weather module")

        for r in range(8):
            self.master.rowconfigure(r, weight=1)
        for c in range(15):
            self.master.columnconfigure(c, weight=1)

        FrameCurrent = Frame(master, bg="white")
        FrameCurrent.grid(row = 0, column = 0, rowspan = 5, columnspan = 5, sticky = W+E+N+S)
        FrameGraph = Frame(master, bg="blue")
        FrameGraph.grid(row = 5, column = 0, rowspan = 5, columnspan = 10, sticky = W+E+N+S)
        FrameD1 = Frame(master, bg="green")
        FrameD1.grid(row = 5, column = 0, rowspan = 3, columnspan = 3, sticky = W+E+N+S)
        FrameD2 = Frame(master, bg="green")
        FrameD2.grid(row=5, column=3, rowspan=3, columnspan=3, sticky=W + E + N + S)
        FrameD3 = Frame(master, bg="green")
        FrameD3.grid(row=5, column=6, rowspan=3, columnspan=3, sticky=W + E + N + S)
        FrameD4 = Frame(master, bg="green")
        FrameD4.grid(row=5, column=9, rowspan=3, columnspan=3, sticky=W + E + N + S)
        FrameD5 = Frame(master, bg="green")
        FrameD5.grid(row=5, column=12, rowspan=3, columnspan=3, sticky=W + E + N + S)

        Label(FrameCurrent, text=self.weatherinfo.currentInfo["Day"], bg = "white", fg = "blue", font=("Helvetica",10)).grid(column=0, row=0, columnspan=5, sticky = W + E)
        Label(FrameCurrent, text=str(self.weatherinfo.currentInfo["Temp"]) + " °C", bg = "white", fg = "blue", font=("Helvetica",16)).grid(column=3, row=1, columnspan=2, rowspan=2, sticky=S)

root = Tk()
app = Application(master=root)
app.mainloop()