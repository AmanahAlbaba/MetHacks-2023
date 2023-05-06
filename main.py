import PySimpleGUI as sg

# see all the themes
#sg.theme_previewer()

projectName = 'MetHacks 2023'

sg.theme('LightBlue')   # Add a touch of color
# All the stuff inside your window.
# layout contains all the visible elements on the screen
# each list is its own row
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok')] ]

# Create the Window
window = sg.Window(f'{projectName}', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

window.close()