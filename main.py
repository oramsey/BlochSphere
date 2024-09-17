import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import tkinter
from tkinter import LEFT, END, DISABLED, NORMAL
import numpy as np


# Define window
window = tkinter.Tk()
window.title ("Qubit Visualization")

# Set the icon
window.iconbitmap(default = 'q.ico')
window.geometry('399x410')
window.resizable(0,0) # Stops resizing

# Define fonts and colors
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial', 18)
display_font = ('Arial', 18)

# intialize the quantum circut
# pre: call the function
# post: intialize the circut variable to state 1
def initialize_circut():
    global circuit
    circuit = QuantumCircuit(1)
    
initialize_circut()
theta = 0

# define functions 
def display_gate(gate_input):
    
    # insert gate
    display.insert(END,gate_input)
    
    # Check if the number of operations is less than 10
    # if not disable gate buttons
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates = list(input_gates)
    search_word = ["R","D","x","y","z","t","s","h"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed = sum(count_double_valued_gates)
    if num_gates_pressed == 10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, Sd_gate,t_gate, Td_gate, hadamard]
        for gate in gates:
            gate.config(state=DISABLED)

def change_theta(num,window,circuit,key):
    global theta
    theta = num * np.pi
    if key == 'x':
        circuit.rx(theta,0)
        theta = 0
    elif key == 'y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta,0)
        theta = 0
    window.destroy()
            
def clear(circuit):
    #clear display
    display.delete(0, END)
    
    #reset the circuit to intial state
    initialize_circut()
    
    #checks if the buttons are disabled and if so, enables them
    if x_gate['state']==DISABLED:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, Sd_gate,t_gate, Td_gate, hadamard]
        for gate in gates:
            gate.config(state=NORMAL)
            
def user_input(circut,key):
    
    #intialize window
    get_input = tkinter.Tk()
    get_input.title('Get Theta')
    get_input.geometry('360x160')
    get_input.resizable(0,0)
    
    val1 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='PI/4',command=lambda:change_theta(0.25,get_input, circuit, key))
    val1.grid(row=0, column=0)
    
    val2 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='PI/2',command=lambda:change_theta(0.5,get_input, circuit, key))
    val2.grid(row=0, column=1)
    
    val3 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='PI',command=lambda:change_theta(1.0,get_input, circuit, key))
    val3.grid(row=0, column=2)
    
    val4 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='2PI',command=lambda:change_theta(2.0,get_input, circuit, key))
    val4.grid(row=0, column=3, sticky = 'W')
    
    
    nval1 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='-PI/4',command=lambda:change_theta(-0.25,get_input, circuit, key))
    nval1.grid(row=1, column=0)
    
    nval2 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='-PI/2',command=lambda:change_theta(-0.5,get_input, circuit, key))
    nval2.grid(row=1, column=1)
    
    nval3 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='-PI',command=lambda:change_theta(-1.0,get_input, circuit, key))
    nval3.grid(row=1, column=2)
    
    nval4 = tkinter.Button(get_input, height=2, width=10, bg=buttons, font=("Arial",10),text='-2PI',command=lambda:change_theta(-2.0,get_input, circuit, key))
    nval4.grid(row=1, column=3, sticky = 'W')
    
def visualize_circuit(circuit, window):
    try:
        visualize_transition(circuit = circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()

# Define frames
display_frame = tkinter.LabelFrame(window)
button_frame = tkinter.LabelFrame(window, bg = 'black' )
display_frame.pack()
button_frame.pack(fill ='both', expand = True)

# Define the display frame layout
display = tkinter.Entry(display_frame, width = 120, font = display_font, bg= background, borderwidth= 10, justify = 'left')
display.pack(padx = 3, pady = 4)

# first button row
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X', command=lambda:[display_gate('x'), circuit.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y', command=lambda:[display_gate('y'), circuit.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z', command=lambda:[display_gate('z'), circuit.z(0)])
x_gate.grid(row=0, column=0, ipadx=45, pady=1)
y_gate.grid(row=0, column=1, ipadx=45, pady=1)
z_gate.grid(row=0, column=2, ipadx=53, pady=1, sticky='E')

# second button row
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rx', command=lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Ry', command=lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rz', command=lambda:[display_gate('Rz'),user_input(circuit,'z')])
Rx_gate.grid(row=1, column=0, columnspan=1, sticky='WE', pady=1)
Ry_gate.grid(row=1, column=1, columnspan=1, sticky='WE', pady=1)
Rz_gate.grid(row=1, column=2, columnspan=1, sticky='WE', pady=1)

# third button row
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S', command=lambda:[display_gate('s'), circuit.s(0)])
Sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD', command=lambda:[display_gate('SD'), circuit.sdg(0)])
hadamard = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H', command=lambda:[display_gate('h'), circuit.h(0)])
s_gate.grid(row=2, column=0, columnspan=1, sticky='WE', pady=1)
Sd_gate.grid(row=2, column=1, columnspan=1, sticky='WE', pady=1)
hadamard.grid(row=2, column=2, rowspan=2, sticky='WENS', pady=1)

# fourth button row
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T', command=lambda:[display_gate('t'), circuit.t(0)])
Td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD', command=lambda:[display_gate('TD'), circuit.tdg(0)])
t_gate.grid(row=3, column=0, columnspan=1, sticky='WE', pady=1)
Td_gate.grid(row=3, column=1, columnspan=1, sticky='WE', pady=1)

# quit and visualize
quit = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Quit', command=window.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Visualize', command=lambda:visualize_circuit(circuit,window))
quit.grid(row=4, column=0, columnspan=2, sticky='WE', ipadx=5,pady=1)
visualize.grid(row=4, column=2, columnspan=1, sticky='WE', ipadx=8, pady=1)

# clear
clear_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='Clear', command=lambda:clear(circuit))
clear_button.grid(row=5, column=0, columnspan=3, sticky='WE')

# about
about_button = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='About')
about_button.grid(row=6, column=0, columnspan=3, sticky='WE')





# Run main loop
window.mainloop()

# X button: flips the state of qubit
# Y button: rotates the state vector about the Y-axis
# Z button: flips the phase by PI radians
# Rx button: parameterized rotation about the X-axis
# Ry button: parameterized rotation about the Y-axis
# Rz button: parameterized rotation about the Z-axis
# T button: rotates the state vector about Z axis by PI/2 radians
# S button: rotates the state vector about Z axis by PI/4 radians
# Sd button: rotates the state vector about Z axis by -PI/2 radians
# Td button: rotates the state vector about Z axis by -PI/4 radians
# H button: creates the state of superpositon 
