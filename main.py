import PySimpleGUI as sg

# see all the themes
#sg.theme_previewer()

projectName = 'MetHacks 2023'


def callAI(input):
    return "testing"



sg.theme('LightBlue')   # Add a touch of color
sg.set_options(font = 'Calibri 20')


# All the stuff inside your window.
# layout contains all the visible elements on the screen
# each list is its own row

button_size = (10,3)

layoutMain = [  [sg.Push(),sg.Text(f'{projectName}', key = '-TEXT1-'), sg.Push()],
            [sg.VPush()],
            [sg.Output(size=(110, 50), font=('Helvetica 10'))],
            [sg.VPush()],
            [sg.Button('Enter', key = '-ENTERBTN-', size = button_size),sg.Multiline(size = (45, 2), key = '-INPUT-')],
            
            [sg.Push(), sg.Button('Report Symptoms', key = '-BTN1-', size = button_size), sg.Button('See Records', key = '-BTN2-', size = button_size), sg.Button('Options', key = '-BTN3-', size = button_size), sg.Push()] ]

layoutOptions = [
    [sg.Push(), sg.Button("Button1"), sg.Push()],
    [sg.Push(), sg.Button("Button2"), sg.Push()],
    [sg.Push(), sg.Button("Button3"), sg.Push()],
    [sg.VPush()],
    [sg.Push(), sg.Button("Return"), sg.Push()]
]

chat = []


# Create the Window
window = sg.Window(f'{projectName}', layoutMain, size = (720, 1280))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break


    if event in ['-ENTERBTN-']:
        chat.append([0,values['-INPUT-']])
        print(f'User: {values["-INPUT-"]}')
        response = callAI(values['-INPUT-'])
        print(f'Bot: {response}')
        chat.append([1, response])
        window['-INPUT-'].update('')





    

    
    
window.close()