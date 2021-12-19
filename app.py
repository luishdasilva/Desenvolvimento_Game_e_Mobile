from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class Grid(Widget):
    pass

class QueroJogar(App):
    def build(self):
        return Builder.load_file('appgame.kv')

QueroJogar().run()
