import tkinter as tk
from PIL import Image, ImageTk
import numpy as numpy
from os import getcwd

import InteractiveAutomata as interactiveAutomata


from initialData.variables_dict import variables_dict


#########
from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders
#########

from tkinter import messagebox, filedialog





# sc = Scale(my_w, from_=0, to=100, font=font1,
#     orient=HORIZONTAL,variable=sv,length=180)
# sc.grid(row=2,column=1,padx=30)


class InitialDataInterface(tk.Frame):
    def __init__(self, border):


        border +=3
        self.root = tk.Tk()
        super().__init__(self.root)


        # definicion de la ventana
        self.root.title('CellularAutomataInterface')
        self.root.geometry('400x400')
        self.root.resizable(width=False, height=False)

 
        # BORDERS
        border_options = []
        for elem in Borders:
            border_options.append( elem.value)
    
        self.border_clicked = tk.StringVar()
        self.border_clicked.set( border_options[0] )
        
        label_border = tk.Label( self.root , text = 'Border:')
        label_border.place(relx=0.1, rely=0.2)
        dropdown_border = tk.OptionMenu( self.root , self.border_clicked , *border_options )
        dropdown_border.place(relx=0.1, rely=0.3, width=120)


        # NEIGHBORHODS
        # neighborhood_options = []
        # for elem in Neighborhoods:
        #     neighborhood_options.append( elem.value)

        neighborhood_options = ['von_Neumann', 'Moore']

        self.neighborhood_clicked = tk.StringVar()
        self.neighborhood_clicked.set( neighborhood_options[0] )
        
        label_neighborhood = tk.Label( self.root , text = 'Neighborhood:')
        label_neighborhood.place(relx=0.4, rely=0.2)
        dropdown_neighborhood = tk.OptionMenu( self.root , self.neighborhood_clicked , *neighborhood_options )
        dropdown_neighborhood.place(relx=0.4, rely=0.3, width=140)


        # NEIGHBORHOD RADIUS (De 1 a infinito)

        self.neighborhood_radius = tk.StringVar()

        label_neighborhood_radius = tk.Label( self.root , text = 'Radius:')
        label_neighborhood_radius.place(relx=0.77, rely=0.2)
        spin_temp = tk.Spinbox(self.root, from_=1, to=100000, textvariable=self.neighborhood_radius)
        spin_temp.place(relx=0.77, rely=0.3, width=70)


        # Store_trace_back
        self.store_trace_back = tk.BooleanVar(value=True)
        label_store_trace_back = tk.Label( self.root , text = 'Radius:')
        label_store_trace_back.place(relx=0.1, rely=0.5)

        self.radiobutton_store_trace_back_yes = tk.Radiobutton(self.root, text="Yes", variable=self.store_trace_back, value=True)
        self.radiobutton_store_trace_back_yes.place(relx=0.3, rely=0.5)
        self.radiobutton_store_trace_back_no = tk.Radiobutton(self.root, text="No", variable=self.store_trace_back, value=False)
        self.radiobutton_store_trace_back_no.place(relx=0.45, rely=0.5)


        # Ruta
        self.initial_data_file_path = ''
        button_set_path = tk.Button( self.root , text = "Set path" , command = self.ask_file_route )
        button_set_path.place(relx=0.1, rely=0.6)
        label_set_path_static = tk.Label( self.root , text = 'path to the folder with the initial state:')
        label_set_path_static.place(relx=0.4, rely=0.6)

        self.label_initial_data_file_path = tk.Label( self.root , text='# Define path to initial data file')#, background=_Color('red'))
        self.label_initial_data_file_path.place(relx=0.4, rely=0.7)

        

        # # Create button, it will change label text
        button = tk.Button( self.root , text = "Start" , command = self.show )
        button.place(relx=0.32, rely=0.9, width=140)

# ACABAR



        
    def ask_file_route(self, event=None):
            # /Users/paul/Desktop/CellularAutomata/initialData
        self.initial_data_file_path = filedialog.askdirectory()
        print('path to folder:', self.initial_data_file_path)
        if (self.initial_data_file_path == '') or (self.initial_data_file_path is None):
            self.label_initial_data_file_path['text'] = '# Define path to initial data file'

        else:
            self.label_initial_data_file_path['text'] = self.initial_data_file_path


    # def radiobutton_command(self):
    #     if self.store_trace_back:
    #         self.radiobutton_store_trace_back.deselect()
    #         print('DESELECCIONADO')
    #     self.store_trace_back = not self.store_trace_back

    #     print(self.store_trace_back)




    def show(self):
        # print(self.border_clicked.get())

        # print(self.neighborhood_clicked.get())

        # print(self.neighborhood_radius.get())

        if self.neighborhood_radius.get().isdigit() and (int(self.neighborhood_radius.get()) >= 1) :

            self.root.destroy()
        else:
            messagebox.showerror('Error', 'Radius ha de ser un número entero mayor a 0.')
        # print( self.neighborhood_radius.get().isdigit() )



    def get_data(self):

#        ACABAR  CONSEGUIR EL ENUM APROPIADO a partir del nombre

        dictionary = {}

        for elem in Borders:
            if elem.value == self.border_clicked.get():
                dictionary['border'] = elem
                break

        for elem in Neighborhoods:
            if elem.value == self.neighborhood_clicked.get():
                dictionary['neighborhood'] = elem
                break

        dictionary['radius'] =  self.neighborhood_radius.get()


        # Falta esto y 
        dictionary['initial_data_file_path'] = self.initial_data_file_path
        dictionary['store_trace_back'] = self.store_trace_back.get()


        
        return dictionary   # hacer que esto se lea apropiadamente
       



        # # Canvas
        # self.canvas = tk.Canvas(self.window, background='black', relief = tk.RAISED)
        # self.canvas.pack(expand=True,  fill=tk.BOTH)

        # # Barra de informacion
        # bar_labels_info = tk.Frame(self.window, bd=1, relief = tk.RAISED)

        # self.label_image_info = tk.Label(bar_labels_info, text='image info', anchor=tk.E, padx = 10)
        # self.label_image_info.pack(side=tk.LEFT)
        # self.label_mouse_cell_ubication = tk.Label(bar_labels_info, text=('——— (—, —)'), anchor=tk.W, padx = 10)
        # self.label_mouse_cell_ubication.pack(side=tk.RIGHT)

        # bar_labels_info.pack(side=tk.BOTTOM, fill=tk.X)

        # # Barra con botones de control
        # bar_buttons = tk.Frame(self.window, bd=1, relief = tk.RAISED)

        # self.button_back = tk.Button(bar_buttons, text='Back', fg='blue', command=self.back_pressed ) 
        # self.button_back.pack( side = tk.LEFT , fill=tk.X)
        # self.button_next = tk.Button(bar_buttons, text='Next', fg='blue', command=self.next_pressed ) 
        # self.button_next.pack( side = tk.LEFT , fill=tk.X)
        # self.button_reset_zoom = tk.Button(bar_buttons, text='Reset zoom', fg='purple', command=self.reset_zoom ) 
        # self.button_reset_zoom.pack( side = tk.LEFT , fill=tk.X)
        # self.button_automatic_play = tk.Button(bar_buttons, text='Start automatic play', fg='green', command=self.automatic_play ) 
        # self.button_automatic_play.pack( side = tk.LEFT , fill=tk.X)       

        # self.button_start = tk.Button(bar_buttons, text='Start', fg='red', command=self.button_start_pressed ) 
        # self.button_start.pack( side = tk.TOP )

        # bar_buttons.pack(side=tk.BOTTOM, fill=tk.X)

        # # eventos de raton
        # self.window.bind('<Motion>', self.mouse_move)
        # self.window.bind('<Button-1>', self.mouse_click_left)
        # self.window.bind('<B1-Motion>', self.mouse_click_left_and_drag)
        # self.window.bind('<Double-Button-1>', self.show_cell_data)  # doble click de boton izquierdo
        # self.window.bind('<MouseWheel>', self.mouse_wheel_zoom)

        # # Eventos de teclado
        # self.window.bind('<Left>', self.back_pressed)
        # self.window.bind('<BackSpace>', self.back_pressed) # Borrar
        # self.window.bind('<Right>', self.next_pressed)
        # self.window.bind('<space>', self.space_or_return_key_pressed)
        # self.window.bind('<Return>', self.space_or_return_key_pressed) # Enter


        # self.set_image(img)




# Botones y teclado
    def back_pressed(self, event=None):
        if not self.auto_play:

            new_image_path = self.automata.back_image_iteration()
            if not (new_image_path is None):
                self.set_image(new_image_path)

    def next_pressed(self, event=None):
        if not self.auto_play or (event == True):
            new_image_path = self.automata.next_image_iteration()
            self.set_image(new_image_path)
            if not self.automata_initialized:
                self.button_start.pack_forget() 
                self.automata_initialized = True

    def button_start_pressed(self, event=None):
        self.automata_initialized = True
        self.reset_zoom()
        self.button_start.pack_forget() 


    def automatic_play(self, event=None):


        if not self.automata_initialized:
            self.button_start_pressed()
        if self.auto_play:
            self.auto_play = False
            self.button_automatic_play['text'] = 'Start automatic play'
            self.button_automatic_play['fg'] = 'green'
            self.button_back['state'] = 'normal'
            self.button_next['state'] = 'normal'

        else:
            self.auto_play = True
            self.button_automatic_play['text'] = 'Stop automatic play'
            self.button_automatic_play['fg'] = 'red'
            self.button_back['state'] = 'disabled'
            self.button_next['state'] = 'disabled'
            self.window.after(1000, self.automatic_next)


    def automatic_next(self):
        if self.auto_play:
            self.next_pressed(True)
            self.window.after(1000, self.automatic_next)


    def space_or_return_key_pressed(self, event=None):
        if  self.automata_initialized:
            self.next_pressed()
        else:
            self.button_start_pressed()


# eventos del raton
    def mouse_click_left(self, event=None):
         # Se guardan posiciones en caso de arrastrar la imagen
        self.last_click_x = event.x
        self.last_click_y = event.y

    def mouse_click_left_and_drag(self, event=None):
        self.translate(event.x - self.last_click_x, event.y - self.last_click_y)
        self.draw_image() 
        self.last_click_x = event.x
        self.last_click_y = event.y

    def mouse_move(self, event=None):
        # Se obtiene las coordenadas del pixel de la imagen
        mat_inv = numpy.linalg.inv(self.matriz_affin)  # calcula la matriz inversa de la matriz affin
        
      
        x_image, y_image, _ = numpy.dot(mat_inv, (event.x, event.y, 1.0)) # producto escalar

        # Si el raton esta fuera de la imagen
        if  (x_image < 0) or (y_image < 0) or (self.iteration_image.width <= x_image ) \
                    or (self.iteration_image.height <= y_image ):
            self.label_mouse_cell_ubication['text'] = ('——— (—, —)')
        else:
            state = self.automata.get_cell(int(x_image), int(y_image)).get_state()
            self.label_mouse_cell_ubication['text'] = str(state) + ' ('+ str( int(x_image) )+', '+str(int( y_image ))+')'




   

    def mouse_wheel_zoom(self, event=None):
        self.translate(-event.x, -event.y)
        if (event.delta < 0):   # Acerca la imagen
            self.scale(1.25)
        else:                   # Aleja la imagen
            self.scale(0.8)
        self.translate(event.x, event.y)
        self.draw_image()


    # Se llama al hacer dobleclick o pulsar start
    def reset_zoom(self, event=None): 
        self.set_zoom()
        self.draw_image()
        self.button_start.pack_forget() 


    def show_cell_data(self, event=None):
        mat_inv = numpy.linalg.inv(self.matriz_affin)  # calcula la matriz inversa de la matriz affin
        x_image, y_image, _ = numpy.dot(mat_inv, (event.x, event.y, 1.0)) # producto escalar
        x_image = int(x_image)
        y_image = int(y_image)
        
        # Si el raton esta fuera de la imagen
        if  (x_image < 0) or (y_image < 0) or (self.iteration_image.width <= x_image ) \
                    or (self.iteration_image.height <= y_image ):
            return

        var_window = tk.Toplevel()
        var_window.geometry('300x200')
        title = 'Cell: (' + str(x_image) + ', ' + str(y_image) + ') iteration: ' + str(self.automata.actual_iteration)
        var_window.title(title)

        var_list = tk.Listbox(var_window, width=300, height=200)
        var_list.place(x=0, y=0)
        var_list.pack(expand=True, fill=tk.BOTH)

        c = self.automata.get_cell( x_image, y_image )

        contador = 0
        for var_name in variables_dict:
            value = c.get_variable(var_name)
            entrada = var_name + ': ' + str(value)
            var_list.insert(contador, entrada)
            contador += 1

        var_list.place(x=0, y=0)

    





    def set_image(self, filename):
        self.iteration_image = Image.open(filename)
        self.set_zoom()
        self.draw_image()
        
        # Actualiza la información de la imagen en la bar_labels_info
        self.label_image_info['text'] = str(self.iteration_image.width)+ ' x ' + \
            str(self.iteration_image.height) + ' itetation: ' + str(self.automata.actual_iteration)


    # Transformación afín para visualización de imágenes.
    def translate(self, offset_x, offset_y):
        matrix = numpy.eye(3)
        matrix[0, 2] = float(offset_x)
        matrix[1, 2] = float(offset_y)
        self.matriz_affin = numpy.dot(matrix, self.matriz_affin) # producto escalar

    def scale(self, scale:float):
        matrix = numpy.eye(3)
        matrix[0, 0] = scale
        matrix[1, 1] = scale
        self.matriz_affin = numpy.dot(matrix, self.matriz_affin) # producto escalar


    def set_zoom(self):
        image_width = self.iteration_image.width
        image_height = self.iteration_image.height

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        # if (image_width * image_height <= 0) or (canvas_width * canvas_height <= 0):
        #     return
        self.matriz_affin = numpy.eye(3)

        scale = 1.0
        offsetx = 0.0
        offsety = 0.0

        # se encaja la imagen a la dimension del canvas mas pequeña
        if (canvas_width * image_height) > (image_width * canvas_height):
            scale = canvas_height / image_height
            offsetx = (canvas_width - image_width * scale) / 2
        else:
            scale = canvas_width / image_width
            offsety = (canvas_height - image_height * scale) / 2

        self.scale(scale)
        self.translate(offsetx, offsety)



    def draw_image(self):
        inverse_matrix = numpy.linalg.inv(self.matriz_affin)
        affine_inv = (inverse_matrix[0, 0], inverse_matrix[0, 1], inverse_matrix[0, 2], \
                      inverse_matrix[1, 0], inverse_matrix[1, 1], inverse_matrix[1, 2])

        image_info = self.iteration_image.transform( (self.canvas.winfo_width(), self.canvas.winfo_height()), \
            Image.Transform.AFFINE, affine_inv, Image.Resampling.NEAREST)

        img = ImageTk.PhotoImage(image_info)
        self.canvas.create_image(0, 0, anchor='nw', image=img)
        self.image = img


