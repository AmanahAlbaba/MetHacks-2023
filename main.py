import PySimpleGUI as sg

# see all the themes
#sg.theme_previewer()

projectName = 'MetHacks 2023'

sg.theme('LightBlue')   # Add a touch of color
# All the stuff inside your window.
# layout contains all the visible elements on the screen
# each list is its own row
layout = [  [sg.Text('Some text on Row 1', key = '-TEXT1-')],
            [sg.Text('Enter something on Row 2'), sg.InputText(key = '-INPUT-')],
            [sg.Button('Ok', key = '-BUTTON1-')] ]

# Create the Window
window = sg.Window(f'{projectName}', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    print(event)
    print(values)

    if event == '-BUTTON1-':
        print('Hello!')
        # update the text
        window['-TEXT1-'].update('WOWOWOWOWOOWOW')

    
window.close()