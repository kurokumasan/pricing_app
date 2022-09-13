from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp

import webbrowser

from pricing import price_estimation, price_detailed

# for testing
#data = [[str(_) for _ in range(6)] for i in range(30)]
data = []

class EstimationScreen(Screen):
    def switch_settlement(self):
        print('switch to settlement mode')
        App.get_running_app().root.current = 'Settlement'

    def switch_description(self):
        print('switch to description mode')
        App.get_running_app().root.current = 'Description'

    def switch_comparison(self):
        print('switch to comparison mode')
        App.get_running_app().root.current = 'Comparison'


    def calculation(self, place, cost, host, host_no, guests, songs, group, guest_stage):
        if place == '':
            place = ''
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
        
        response, record =  price_estimation(\
                int(cost), \
                int(host), \
                int(host_no), \
                int(guests), \
                int(songs), \
                int(group), \
                int(guest_stage), \
                place)
        print(record)

        global data
        if len(data) == 0 or record != data[-1]:
            data.append(record)

        return response

class SettlementScreen(Screen):
    def switch_estimation(self):
        print('switch to estimation mode')
        App.get_running_app().root.current = 'Estimation'

    def switch_description(self, source):
        print('switch to description mode')
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
    def __init__(self, **kwargs):
        super(DescriptionScreen, self).__init__(**kwargs)
        win_size = Window.size
        self.scale = min(win_size[0]/self.ids.desc.texture_size[0], win_size[1]/self.ids.desc.texture_size[1])

        # get desc real size
        shift_x = self.scale * self.ids.desc.texture_size[0]
        shift_y = self.scale * self.ids.desc.texture_size[1]

        # yt icon
        self.ids.yt.size = shift_x*0.12, shift_y*0.06
        self.ids.yt.x = win_size[0]*0.5 + shift_x*0.04
        self.ids.yt.y = win_size[1]*0.55 + shift_y*0.23

        # drive icon
        self.ids.drive.size = shift_x*0.12, shift_y*0.06
        self.ids.drive.x = win_size[0]*0.5 + shift_x*0.05
        self.ids.drive.y = win_size[1]*0.55 - shift_y*0.38

    def switch_estimation(self):
        print('switch to estimation mode')
        App.get_running_app().root.current = 'Estimation'

    def switch_settlement(self):
        print('switch to settlement mode')
        App.get_running_app().root.current = 'Settlement'

    def on_enter(self):
        win_size = Window.size
        self.scale = min(win_size[0]/self.ids.desc.texture_size[0], 0.9*win_size[1]/self.ids.desc.texture_size[1])

        # get desc real size
        shift_x = self.scale * self.ids.desc.texture_size[0]
        shift_y = self.scale * self.ids.desc.texture_size[1]

        # yt icon
        self.ids.yt.size = shift_x*0.14, shift_y*0.07
        self.ids.yt.x = win_size[0]*0.5 + shift_x*0.04
        self.ids.yt.y = win_size[1]*0.55 + shift_y*0.25

        # drive icon
        self.ids.drive.size = shift_x*0.14, shift_y*0.07
        self.ids.drive.x = win_size[0]*0.5 + shift_x*0.05
        self.ids.drive.y = win_size[1]*0.55 - shift_y*0.42

        print(self.scale, shift_x, shift_y, self.ids.desc.pos, self.size)

    def go_to_yt(self):
        webbrowser.open('https://www.youtube.com')
        print('yt!')

    def go_to_drive(self):
        webbrowser.open('https://drive.google.com')
        print('drive!')

class ComparisonScreen(Screen):
    def __init__(self, **kwargs):
        super(ComparisonScreen, self).__init__(**kwargs)
        global data
        for i in data:
            d = {f'label{idx+1}': str(j) for idx,j in enumerate(i)}
            print(str(d))
            self.rv.data.append(d)

    def on_enter(self):
        self.draw()

    def draw(self):
        self.rv.data = []
        print('redraw view')
        global data
        for i in data:
            d = {f'label{idx+1}': str(j) for idx,j in enumerate(i)}
            print(str(d))
            self.rv.data.append(d)

    def switch_estimation(self):
        print('switch to estimation mode')
        App.get_running_app().root.current = 'Estimation'
    
    def clean_memory_then_go_back(self):
        global data
        data = []
        self.rv.data = []
        App.get_running_app().root.current = 'Estimation'

class PricingApp(App):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(DescriptionScreen(name='Description'))
        self.sm.add_widget(ComparisonScreen(name='Comparison'))
        self.sm.add_widget(EstimationScreen(name='Estimation'))
        self.sm.add_widget(SettlementScreen(name='Settlement'))

        return self.sm


if __name__ == '__main__':
    LabelBase.register(name='NotoSansCJK',fn_regular='font/NotoSansCJKtc-Regular.otf')
    #Window.size = (640,960)
    PricingApp().run()
