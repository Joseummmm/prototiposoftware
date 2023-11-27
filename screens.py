import tkinter as tk
from constantes import styles,config
import json
import os
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk, Image
from tkinter import messagebox
import numpy as np

class home(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background = styles.fondo)
        self.controller = controller
        self.opcionElegida = tk.StringVar(self,value="Configuracion")
      
        self.init_widgets()

    def move_to_config(self):
        self.controller.opcion = self.opcionElegida
        self.controller.show_frame(ConfiguracionInvernadero)

    def move_to_VerConfig(self):

        self.controller.show_frame(verConfiguracion)

    def move_to_verAlerta(self):
        self.controller.show_frame(verAlerta)

    def init_widgets(self):
        tk.Label(self,text="ProyectoSoftware",justify=tk.CENTER,**styles.estilo).pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        optionsFrame= tk.Frame(self)
        optionsFrame.configure (background=styles.fondo)
        optionsFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        tk.Label(optionsFrame,text="Seleccione una opción",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        
        tk.Button(self,text=" Configuración",command=self.move_to_config,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )
        tk.Button(self,text=" Ver configuración",command=self.move_to_VerConfig,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )
        tk.Button(self,text=" Ver Alerta",command=self.move_to_verAlerta,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )
class ConfiguracionInvernadero(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background = styles.fondo1)
        self.controller = controller
        self.opcionElegidaInvernadero = tk.StringVar(self)

        self.init_widgets()

    def move_to_configCultivo(self):
        self.controller.opcionInvernadero = self.opcionElegidaInvernadero.get(),
        print(self.controller.opcionInvernadero)
        self.controller.opcionInvernadero = self.opcionElegidaInvernadero.get(),
        self.controller.show_frame(ConfiguracionCultivo)

    
    def init_widgets(self):
        tk.Label(self,text="ProyectoSoftware",justify=tk.CENTER,**styles.estilo).pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        optionsFrame= tk.Frame(self)
        optionsFrame.configure (background=styles.fondo)
        optionsFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        tk.Label(optionsFrame,text="Seleccione su tipo de invernadero",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        for (key,value) in config.configuracionInvernadero.items():
            tk.Radiobutton(
                optionsFrame,
                text = key,
                variable=self.opcionElegidaInvernadero,
                value=value,
                activebackground=styles.fondo1,
                activeforeground=styles.TEXTCUERPO
            ).pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=5,pady=5)
        tk.Button(self,text="Siguiente",command=self.move_to_configCultivo,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )

class ConfiguracionCultivo(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background = styles.fondo1)
        self.controller = controller
        self.opcionElegidaCultivo = tk.StringVar(self,value="")

        self.init_widgets()

    def move_to_configRiego(self):
        index = 0
        self.ArrayVarAux = self.ArrayVar.copy()
        for i in self.ArrayVar:
            self.ArrayVarAux[index] = i.get()
            index += 1
        self.controller.opcionesCultivo = self.ArrayVarAux
        
        self.controller.show_frame(ConfiguracionRiego)

    def print_selection(self):
        count = 0
        lista = config.configuracionCultivo.keys()

        for (i) in lista:
            if(self.ArrayVar[count].get() == 1):
                print("Su cultivo tiene",i)
            else:
                print("Su cultivo no tiene",i)
            count = count +1 

    def init_widgets(self):
        tk.Label(self,text="ProyectoSoftware",justify=tk.CENTER,**styles.estilo).pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        optionsFrame= tk.Frame(self)
        optionsFrame.configure (background=styles.fondo)
        optionsFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        tk.Label(optionsFrame,text="Seleccione el tipo de cultivos presentes en el invernadero",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var4 = tk.IntVar()
        var5 = tk.IntVar()
        var6 = tk.IntVar()
        self.ArrayVar = [var1,var2,var3,var4,var5,var6]
        index = 0
        for (key,value) in config.configuracionCultivo.items():
            tk.Checkbutton(
                optionsFrame,
                text = key,
                variable = self.ArrayVar[index],
                onvalue=1,
                offvalue=0
            ).pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=5,pady=5)
            index = index + 1
        tk.Button(self,text="Siguiente",command=self.move_to_configRiego,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )
 # CAMBIAR A ESTE COMANDO PARA VERIFICAR QUE SE GUARDAN LOS CULTIVOS

class ConfiguracionRiego(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background = styles.fondo1)
        self.controller = controller
        self.opcionElegidaRiego = tk.StringVar(self,value="")

        self.init_widgets()

    def move_to_home(self):
        self.controller.opcionRiego = self.opcionElegidaRiego.get()
        print(self.controller.opcionInvernadero)
        self.controller.show_frame(home)

    def print_selection(self):
        count = 0
        lista = config.configuracionCultivo.keys()
        for (i) in lista:
            if(self.ArrayVar[count].get() == 1):
                print("Su cultivo tiene",i)
            else:
                print("Su cultivo no tiene",i)
            count = count +1 

    def init_widgets(self):
        tk.Label(self,text="ProyectoSoftware",justify=tk.CENTER,**styles.estilo).pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        optionsFrame= tk.Frame(self)
        optionsFrame.configure (background=styles.fondo)
        optionsFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        tk.Label(optionsFrame,text="Seleccione el tipo de riego para su invernadero",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        index = 0
        for (key,value) in config.configuracionRiego.items():
            tk.Radiobutton(
                optionsFrame,
                text = key,
                variable=self.opcionElegidaRiego,
                value=value,
                activebackground=styles.fondo1,
                activeforeground=styles.TEXTCUERPO
            ).pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=5,pady=5)
            index = index + 1
        tk.Button(self,text="Siguiente",command=self.move_to_home,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )

class verConfiguracion(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background = styles.fondo1)
        self.controller = controller
        self.opcionElegida = tk.StringVar(self,value="")

        self.init_widgets()


    def move_to_home(self):
        
        
        self.controller.show_frame(home)
    
       

    def update(self):
        if(self.controller.opcionInvernadero != ""):
            self.invernadero['text'] = self.controller.opcionInvernadero
        else:
            print("no ha ingresado datos")
        if(self.controller.opcionRiego != ""):
            self.riego['text'] =self.controller.opcionRiego
        
        count = 0
        contadorCultivo = 0
        lista = config.configuracionCultivo.keys()


        for i in lista:
            print(self.controller.opcionesCultivo[count])
            if(self.controller.opcionesCultivo[count]==1):
                if(contadorCultivo == 0):
                    self.cultivos['text'] = ""
                    self.cultivos['text'] =  self.cultivos['text'] + i + " "
                elif(count == 6):
                    self.cultivos['text'] =  self.cultivos['text'] + i
                else:
                    self.cultivos['text'] =  self.cultivos['text'] + i + " "
                contadorCultivo += 1
            count = count + 1    

        guardarDatos = [[self.controller.opcionInvernadero],[self.controller.opcionRiego],[self.controller.opcionesCultivo]]
        
        carpeta_data = "data"

        if not os.path.exists(carpeta_data):
            os.makedirs(carpeta_data)

        ruta_json = os.path.join(carpeta_data, "opciones.json")

        with open(ruta_json, "w") as json_file:
            json.dump(guardarDatos, json_file)

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Guardado", "Opciones guardadas exitosamente en 'opciones.json'")    


    def init_widgets(self):
        tk.Label(self,text="ProyectoSoftware",justify=tk.CENTER,**styles.estilo).pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        optionsFrame= tk.Frame(self)
        optionsFrame.configure (background=styles.fondo)
        optionsFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        tk.Label(optionsFrame,text="Su configuración es:",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        valor = self.controller.opcionInvernadero
        opcion = self.controller.opcionInvernadero
        opcionRiego = self.controller.opcionRiego   
        opcionCultivo = self.controller.opcionesCultivo

        tk.Label(optionsFrame,text="Tipo de invernadero",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)       
        self.invernadero = tk.Label(optionsFrame,text=opcion,justify=tk.CENTER,**styles.estiloCuerpo)
        self.invernadero.pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)

        tk.Label(optionsFrame,text="Cultivos",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        self.cultivos = tk.Label(optionsFrame,text=opcionCultivo,justify=tk.CENTER,**styles.estiloCuerpo)
        self.cultivos.pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)

        tk.Label(optionsFrame,text="Método de riego",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        self.riego = tk.Label(optionsFrame,text=opcionRiego,justify=tk.CENTER,**styles.estiloCuerpo)
        self.riego.pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        tk.Button(self,text="Volver al menú",command=self.move_to_home,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )
        tk.Button(self,text="Actualizar",command=self.update,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            fill= tk.X,
            padx=22,
            pady=11
        )


class verAlerta(tk.Frame):

    def __init__(self,parent,controller):
        super().__init__(parent)
        self.configure(background = styles.fondo1)
        self.controller = controller
        self.opcionElegida = tk.StringVar(self,value="")
        
        self.init_widgets()


    def move_to_home(self):
        self.controller.show_frame(home)
    
    def init_widgets(self):
        tk.Label(self,text="ProyectoSoftware",justify=tk.CENTER,**styles.estilo).pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        optionsFrame= tk.Frame(self)
        img = Image.open("src/Gota de agua.png")
        imgDanger = Image.open("src/danger.png")
        dangerResize = imgDanger.resize((150,150))
        resize_img = img.resize((150,150))
        optionsFrame.configure (background="white")
        optionsFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        tk.Label(optionsFrame,text="Ejemplo de alerta",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)
        

        tk.Label(optionsFrame,text="ATENCIÓN",justify=tk.CENTER,**styles.estiloAlerta).pack(side=tk.TOP,fill=tk.X,padx=22,pady=11)       
        tk.Label(optionsFrame,text="Su Albahaca necesita riego",justify=tk.CENTER,**styles.estiloCuerpo).pack(side=tk.TOP,padx=22,pady=11)      
        imagenLista = ImageTk.PhotoImage(resize_img) 
        imagen = tk.Label(optionsFrame,image= imagenLista,borderwidth=0,highlightthickness=0)
        imagen.pack()
        imagen.photo = imagenLista  
        
        dangerLista = ImageTk.PhotoImage(dangerResize)
        dangerImage = tk.Label(optionsFrame,image= dangerLista,borderwidth=0,highlightthickness=0)
        dangerImage.pack(side="left")
        dangerImage.photo = dangerLista
        
        tk.Button(self,text="Entendido",command=self.move_to_home,**styles.estiloCuerpo,relief=tk.FLAT,activebackground=styles.fondo,activeforeground=styles.TEXTCUERPO).pack(
            side=tk.TOP,
            
            padx=22,
            pady=11
        )