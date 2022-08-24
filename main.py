from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.text import LabelBase

from pricing import price_estimation, price_detailed


class EstimationScreen(Screen):
    def switch_settlement(self):
        print('switch to settlement mode')
        App.get_running_app().root.current = 'Settlement'

    def switch_description(self):
        print('switch to description mode')
        App.get_running_app().root.current = 'Description'

    def calculation(self, cost, host, host_no, guests, songs, group, guest_stage):
        if cost == '':
            return f'總成本不可為0'
        if host == '':
            return f'主辦人數不可為0'
        if host_no == '':
            host_no = '0'
        if guests == '':
            guests = '0'
        if songs == '':
            return f'歌曲總數不可為0'
        if group == '':
            return f'平均編制人數不可為0'
        if guest_stage == '':
            guest_stage = '0'
        
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

    def switch_description(self, source):
        print('switch to description mode')
        DescriptionScreen().set_source(source)
        App.get_running_app().root.current = 'Description'

    def calculation(self, cost, host, host_no, guests, all_stages, guest_stages):
        if cost == '':
            return f'總成本不可為0'
        if host == '':
            return f'主辦人數不可為0'
        if host_no == '':
            host_no = '0'
        if guests == '':
            return f'協辦人數不可為0'
        if all_stages == '':
            return f'全員總上台數不可為0'
        if guest_stages == '':
            guest_stages = '0'

        return price_detailed(\
                int(cost), \
                int(host), \
                int(host_no), \
                int(guests), \
                int(all_stages), \
                int(guest_stages))

class DescriptionScreen(Screen):
    def switch_estimation(self):
        print('switch to estimation mode')
        App.get_running_app().root.current = 'Estimation'

    def switch_settlement(self):
        print('switch to settlement mode')
        App.get_running_app().root.current = 'Settlement'

class PricingApp(App):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(DescriptionScreen(name='Description'))
        self.sm.add_widget(EstimationScreen(name='Estimation'))
        self.sm.add_widget(SettlementScreen(name='Settlement'))

        return self.sm


if __name__ == '__main__':
    LabelBase.register(name='NotoSansCJK',fn_regular='font/NotoSansCJKtc-Regular.otf')
    PricingApp().run()
