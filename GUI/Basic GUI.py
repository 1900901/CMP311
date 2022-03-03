import PySimpleGUI as sg

def DashboardButton():
    frDashboard.unhide_row()

def ScanButton():
    frDashboard.hide_row()

def ResultsButton():
    frDashboard.hide_row()

def ExampleButton():
    frDashboard.hide_row()

def ExampleButton2():
    frDashboard.hide_row()



sg.theme('DarkBlue13')

frDashboard = sg.Frame("", [
    [sg.Text("⚠", font=(None, 200), text_color="#ff9500"),],
    [sg.Text("5", font=(None, 15), text_color="red", pad=(0, 0)), sg.Text("Warnings", font=(None, 15), pad=(0, 0))]
    ], relief="flat", size=(552 , 440), element_justification='c')


RowMenu = sg.Frame("", [[
    sg.Image("..\Images\Abertay_University_Logo.svg.png", subsample=50, size=(30, 30)),
    sg.Text("Smallwood Rugby: Network Security Scanner")
    ]], size=(640 , 40), relief="flat")

#RowMenu.grab_anywhere_include()

col1 = sg.Column([
    [sg.Button("Dashboard", key=DashboardButton, size=(10,5), button_color="#202940", pad=(0, 0))],
    [sg.Button("Scan", key=ScanButton, size=(10,5), button_color="#202940", pad=(0, 0))],
    [sg.Button("Results", key=ResultsButton, size=(10,5), button_color="#202940", pad=(0, 0))],
    [sg.Button("Example", key=ExampleButton, size=(10,5), button_color="#202940", pad=(0, 0))],
    [sg.Button("Another Example", key=ExampleButton2, size=(10,5), button_color="#202940", pad=(0, 0))]
    ], pad=(0, 0), size=(88, 440))

colMain = sg.Column([
    [frDashboard]
    ], pad=(0, 0), size=(552 , 440))

layout = [
    [RowMenu],
    [col1, colMain]
    ]

# Create the Window
window = sg.Window('CMP311 Test Application', layout, margins=(0,0)) # use_custom_titlebar="true")
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if callable(event):
        event()

window.close()