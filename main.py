from kivy.app import App
#from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from pricing import price_estimation, price_detailed


class EstimationScreen(Screen):
    def switch_settlement(self):
        print('switch to settlement mode')
        App.get_running_app().root.current = 'Settlement'

class SettlementScreen(Screen):
    def switch_estimation(self):
        print('switch to estimation mode')
        App.get_running_app().root.current = 'Estimation'

class PricingApp(App):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(EstimationScreen(name='Estimation'))
        self.sm.add_widget(SettlementScreen(name='Settlement'))

        return self.sm


if __name__ == '__main__':
    PricingApp().run()
