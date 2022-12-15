import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="Enter some text:"))

        self.text_input = TextInput(multiline=False)
        self.add_widget(self.text_input)

        self.display_label = Label(text="")
        self.add_widget(self.display_label)

        self.submit_button = Button(text="Submit", on_press=self.on_submit)
        self.add_widget(self.submit_button)

        self.clear_button = Button(text="Clear", on_press=self.on_clear)
        self.add_widget(self.clear_button)

    def on_submit(self, instance):
        text = self.text_input.text
        self.display_label.text = text

    def on_clear(self, instance):
        self.text_input.text = ""
        self.display_label.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
