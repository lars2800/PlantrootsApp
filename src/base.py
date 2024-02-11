from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy


kivy.require("1.9.0")

class KivyTest(App):

    def build(self):
        return BoxLayout()


if __name__ == '__main__':
    KivyTest().run()