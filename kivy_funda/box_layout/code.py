import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def OutputMsg(self):
        print(f"Name: {self.name.text} Email: {self.email.text}")
        self.name.text = ""
        self.email.text = ""

    def ClearMsg(self):
        self.name.text = ""
        self.email.text = ""



class MyApp(App):
    def build(self):
        return BoxLayout()


if __name__ == "__main__":
    MyApp().run()


