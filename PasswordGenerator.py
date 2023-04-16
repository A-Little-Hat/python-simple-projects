import PySimpleGUI as sg
import random
import pyperclip

def generate(psdlen):
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=+*&^%$#@!:;~`_][?.-)(0123456789"
    password=""
    for i in range(psdlen):
        password=password+random.choice(chars)
    return password


sg.theme('Darkamber')
buttons = [[sg.Submit('Generate', auto_size_button=True)]]

layout = [
    [sg.Text('Password Generator', font=('Arial Bold', 30),
             size=25,
             expand_x=True,
             justification='center')],
    [sg.Text('Specify the length of the password', font=('Arial Bold', 10),
             size=20,
             expand_x=True,
             justification='center'),sg.InputText()],
    [sg.Column(buttons, justification='center')]
]

window = sg.Window('Password Generator', layout, resizable=True).Finalize()

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Generate':
        if values[0] !='':
            length = int(values[0])
            print(length)
            psd=generate(int(length))
            print(psd)
            sg.popup_ok("Password is : ",psd)
            pyperclip.copy(psd)
            sg.popup("Copied to clipboard")
        else:
            sg.popup_error('Enter Valid Integer')
            
window.close()
