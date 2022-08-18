from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.text import LabelBase

from pricing import price_estimation, price_detailed


class EstimationScreen(Screen):
    def switch_settlement(self):
        print('switch to settlement mode')
        App.get_running_app().root.current = 'Settlement'

    def calculation(self, cost, host, host_no, guests, songs, group, guest_stage):
        return price_estimation(\
                int(cost), \
                int(host), \
                int(host_no), \
                int(guests), \
                int(songs), \
                int(group), \
                int(guest_stage))

class SettlementScreen(Screen):
    def switch_estimation(self):
        print('switch to estimation mode')
        App.get_running_app().root.current = 'Estimation'
    def calculation(self, cost, host, host_no, guests, all_stages, guest_stages):
        return price_detailed(\
                int(cost), \
                int(host), \
                int(host_no), \
                int(guests), \
                int(all_stages), \
                int(guest_stages))

class PricingApp(App):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(EstimationScreen(name='Estimation'))
        self.sm.add_widget(SettlementScreen(name='Settlement'))

        return self.sm


if __name__ == '__main__':
    LabelBase.register(name='NotoSans',\
            fn_regular='/usr/share/fonts/truetype/notosans/NotoSans-Regular.ttf',\
            fn_bold='/usr/share/fonts/truetype/notosans/NotoSans-Bold.ttf',\
            fn_italic='/usr/share/fonts/truetype/notosans/NotoSans-Italic.ttf',\
            fn_bolditalic='/usr/share/fonts/truetype/notosans/NotoSans-BoldItalic.ttf'\
            )

    PricingApp().run()
