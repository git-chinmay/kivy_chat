from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file('textinputtest.kv')

class AnswerInput(BoxLayout):
    pass

class TextInputTest(App): # If your kv file is called textinputtest.kv

    def build(self):
        return AnswerInput()

if __name__ == '__main__':
    TextInputTest().run()