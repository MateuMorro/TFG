from tkinter import *
from tkinter import messagebox

class Inici:

    def __init__(self):


        self.__ventana = Tk()
        self.__option=IntVar(value=1)

        self.__circuit=IntVar(value=1)
        self.__simulaciones=IntVar(value=1)
        self.__usuari=IntVar(value=1)
        colorFondo="#000000"
        colorLletra="#FFF"
        self.__ventana.title("Car Machine Learning")
        self.__ventana.geometry("740x550")
        self.__ventana.configure(background=colorFondo)

        Label(self.__ventana,text="Benvingut! Es troba en Car Machine Learning on els cotxes han entrenat mitjançant l'aprenentatge supervisat.",
                                     bg=colorFondo, fg=colorLletra).place(x=50, y=10)
        Label(self.__ventana,text="Els cotxes s'han entrenat en 12 circuits. Els circuits 13,14 i 15 són els circuits test.",bg=colorFondo,fg=colorLletra).place(x=50,y=50)

        #self.viaje = Spinbox(self.__ventana, from_=1, to=15, wrap=True,textvariable=self.__circuit)

        #self.viaje.pack(padx=30,pady=80)

        Label(self.__ventana,
              text="Elegeixi un circuit (el valor ha de ser un nombre natural entre 1 i 15).",
              bg=colorFondo, fg=colorLletra).place(x=50, y=70)
        Entry(self.__ventana,textvariable=self.__circuit).place(x=50,y=100)

        Label(self.__ventana,
              text="Vol jugar contra el millor cotxe?",
              bg=colorFondo, fg=colorLletra).place(x=50, y=150)
        Label(self.__ventana,
              text="Si vol, hi haurà dos cotxes en el circuit. Utilitzi les fletxes del teclat per accelerar, frenar i girar.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=170)
        Label(self.__ventana,
              text="0 - Si.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=190)
        Label(self.__ventana,
              text="1 - No.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=210)
        Entry(self.__ventana, textvariable=self.__usuari).place(x=50, y=240)



        Label(self.__ventana,
              text="L'entrenament s'ha dut a terme en funció del nombre d'iteracions i de eta.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=290)

        Label(self.__ventana,
              text="Les següents combinacions són les millors. Introdueixi la combinació (valor enter entre 1 i 4):",
              bg=colorFondo, fg=colorLletra).place(x=50, y=310)
        Label(self.__ventana,
              text="* Combinació 1:    220 iteracions i eta=0.02",
              bg=colorFondo, fg=colorLletra).place(x=50, y=330)
        Label(self.__ventana,
              text="* Combinació 2:    265 iteracions i eta=0.027",
              bg=colorFondo, fg=colorLletra).place(x=50, y=350)
        Label(self.__ventana,
              text="* Combinació 3:    269 iteracions i eta=0.0275",
              bg=colorFondo, fg=colorLletra).place(x=50, y=370)
        Label(self.__ventana,
              text="* Combinació 4:    600 iteracions i eta=0.07",
              bg=colorFondo, fg=colorLletra).place(x=50, y=390)
        Entry(self.__ventana, textvariable=self.__option).place(x=50, y=420)



        Label(self.__ventana,
              text="Introdueix el nombre de simulacions (nombre enter major o igual a 1):",
              bg=colorFondo, fg=colorLletra).place(x=50, y=470)
        Entry(self.__ventana, textvariable=self.__simulaciones).place(x=50, y=500)

        Button(self.__ventana,text="Comencem!", command=self.start, bg="#000000",fg="white").place(x=560,y=500)

        mainloop()


    def start(self):
        return self.__ventana.quit()

    def circuit(self):
        return self.__circuit.get()

    def usuari(self):
        return self.__usuari.get()

    def option(self):
        return self.__option.get()
    def simulaciones(self):
        return self.__simulaciones.get()





