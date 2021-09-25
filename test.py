from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (400, 700)

class Main_menu(Screen):
    def change_text(self):
        BoxLayout:
            orientation: 'vertical'
            spacing: 5
            padding: [50, 10]

            Button:
                text: 'Блюдо 1'
                on_press:
                    root.manager.current = 'Menu1'

            Button:
                text: 'Блюдо 2'
                on_press:
                root.manager.current = 'Menu2'

            Button:
                text: 'Блюдо 3'
                on_press:
                root.manager.current = 'Menu3'

            Button:
                text: 'Блюдо 4'
                on_press:
                root.manager.current = 'Menu4'

            Button:
                text: 'Блюдо 5'
                on_press:
                root.manager.current = 'Menu5'
        pass



class Menu1(Screen):
    pass

class TestApp(App):
    pass

if __name__ == '__main__':
    TestApp().run()