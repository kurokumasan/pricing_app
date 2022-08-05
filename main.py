from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from pricing import price_estimation, price_detailed


class PricingGrid(Widget):
    pass

class PricingApp(App):
    def build(self):
        return PricingGrid() 


if __name__ == '__main__':
    PricingApp().run()
