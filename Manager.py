import tkinter as tk
from constantes import styles
from screens import home,ConfiguracionInvernadero,ConfiguracionCultivo,ConfiguracionRiego,verConfiguracion,verAlerta

class Manager(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Menú principal")
        container = tk.Frame(self)
        
        self.opcionInvernadero = "Aún no introduce un tipo de invernadero"
        self.opcionesCultivo = "Aún no introduce al menos un tipo de cultivo"
        self.opcionRiego = "Aún no introduce un método de riego"
        container.pack(
            side= tk.TOP,
            fill= tk.BOTH,
            expand = True
        )
        container.configure(background = styles.fondo)
        container.grid_columnconfigure(0,weight=1)
        container.grid_rowconfigure(0,weight=1)

        self.frames = {}
        for i in (home,ConfiguracionInvernadero,ConfiguracionCultivo,ConfiguracionRiego,verConfiguracion,verAlerta):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0,column=0,sticky=tk.NSEW)
        self.show_frame(home)

    def show_frame(self,container):
        frame = self.frames[container]
        frame.tkraise()