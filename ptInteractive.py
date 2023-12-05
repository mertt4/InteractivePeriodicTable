# json data converted from csv, from https://en.wikipedia.org/wiki/List_of_chemical_elements

import json
import tkinter as tk

def openElement(symbol):
    element_data = ELEMENTS[symbol]
    elementWindow = tk.Toplevel(window)
    elementWindow.geometry("400x300")
    elementWindow.title(symbol)
    
    for idx, key in enumerate(element_data):
        lblInfo = tk.Label(master=elementWindow, text=key)
        lblInfo.grid(row=idx, column=0)

        lblElementData = tk.Label(master=elementWindow, text=element_data[key])
        lblElementData.grid(row=idx, column=1)

        
# Read in all the data from periodictable.json.
# opens the periodic table json in read mode
with open('PeriodicTable.json', 'r', encoding="utf8") as file:
    data = json.load(file)['elements']

# Create a dictionary to store elements with their symbols as keys
ELEMENTS = {element['Symbol']: element for element in data}

#set up window with title, not resizable
window = tk.Tk()
window.title("Periodic Table of Elements")
window.resizable(width=False, height=False)

# create button for each element in the ELEMENTS dictionary
for element_symbol in ELEMENTS:
    element = ELEMENTS[element_symbol]
    if element['Group'] != "":
        btnElement = tk.Button(master=window, text=element['Symbol'], command=lambda symbol=element['Symbol']: openElement(symbol))
        btnElement.grid(row=element['Period'], column=element['Group'], sticky="nsew")
    else:
        btnElement = tk.Button(master=window, text=element['Symbol'], command=lambda symbol=element['Symbol']: openElement(symbol))
        btnElement.grid(row=element['Period']+2, column=(element["Atomic number"]+10)%32, sticky="nsew")

window.mainloop()
