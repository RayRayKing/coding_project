#!python 3
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a little color to your windows

# All the stuff inside your window. This is the PSG magic code compactor...
layout = [ [sg.Text("X starts first")],
[sg.Button("  ",key="1"),sg.Button("  ",key="2"),sg.Button("  ",key="3")],
[sg.Button("  ",key="4"),sg.Button("  ",key="5"),sg.Button("  ",key="6")],
[sg.Button("  ",key="7"),sg.Button("  ",key="8"),sg.Button("  ",key="9")],
[sg.Button("Reset"), sg.Cancel()]]

list_options = [x for x in range (1,10)]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
counter = 0 
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event in str(list_options):
        counter += 1
        player = ""
        if counter % 2 == 0:
            player = "o"
        else:
            player = "x"
        window[event].update(player)
    elif event == "Reset":
        for x in list_options:
            window[str(x)].update("  ")
window.close()

