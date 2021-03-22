from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.uix.dialog import MDDialog
class gridlayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 4
        self.cols = 1
        self.image = Image(source = r"C:\Users\SANJAYA\Downloads\fitness.jpg")
        self.add_widget(self.image)
        self.label = Label(text = "IF YOU WANT TO JOIN, ENTER YOUR DETAILS ON BELOW TEXTBOX ", font_size = 15, color = "purple")
        self.add_widget(self.label)
        self.txt = TextInput(text = " ", font_size = 20)
        self.add_widget(self.txt)

        self.flat_button = MDRectangleFlatButton(text = "SUBMIT", pos_hint = {'center_x':0.3, 'center_y':0.5}, on_release = self.show_data)
        self.add_widget(self.flat_button)


    def show_data(self, obj):
        close_button = MDRectangleFlatButton(text = 'close', on_release = self.close_dialog)
        if self.txt.text == " ":
            dialog1 = MDDialog(text = "please enter the details", title = "error", buttons = [close_button])
            dialog1.open()
        else:
           dialog2 = MDDialog(text = "database not connected,try after some time", title = "gym admission", buttons = [close_button])
           dialog2.open()
    def close_dialog(self, obj):
        dialog1.dismiss()
        dialog2.dismiss()








class demoapp(MDApp):
    def build(self):
       return gridlayout()


demoapp().run()
