import tkinter as tk
from tkinter import messagebox, filedialog

from automata.Neighborhoods import Neighborhoods
from automata.Borders import Borders



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
        label_set_path_static = tk.Label( self.root , text = 'Path to the folder with the initial state:')
        label_set_path_static.place(relx=0.4, rely=0.6)

        self.label_initial_data_file_path = tk.Label( self.root , text='# Define path to initial data file')#, background=_Color('red'))
        self.label_initial_data_file_path.place(relx=0.4, rely=0.7)

        

        # # Create button, it will change label text
        button = tk.Button( self.root , text = "Start" , command = self.end_enter_data )
        button.place(relx=0.32, rely=0.9, width=140)




        
    def ask_file_route(self, event=None):
            # /Users/paul/Desktop/CellularAutomata/initialData
        self.initial_data_file_path = filedialog.askdirectory()
        print('path to folder:', self.initial_data_file_path)
        if (self.initial_data_file_path == '') or (self.initial_data_file_path is None):
            self.label_initial_data_file_path['text'] = '# Define path to initial data file'

        else:
            self.label_initial_data_file_path['text'] = self.initial_data_file_path





    def end_enter_data(self):
        if (self.initial_data_file_path == ''):
            messagebox.showerror('Error', 'The path to the folder with the initial state has not been defined.')

        elif (not self.neighborhood_radius.get().isdigit() ) or (int(self.neighborhood_radius.get()) < 1) :
            messagebox.showerror('Error', 'Radius must be an integer greater than 0.')
            
        else:
            self.root.destroy()



    def get_data(self):
        dictionary = {}

        for elem in Borders:
            if elem.value == self.border_clicked.get():
                dictionary['border'] = elem
                break

        for elem in Neighborhoods:
            if elem.value == self.neighborhood_clicked.get():
                dictionary['neighborhood'] = elem
                break

        dictionary['radius'] =  int(self.neighborhood_radius.get())
        dictionary['initial_data_file_path'] = self.initial_data_file_path
        dictionary['store_trace_back'] = self.store_trace_back.get()


        
        return dictionary
       

