from kivymd.app import MDApp
from kivymd.uix.list import MDList, ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from screen_nav import toolbar_helper

Window.size = (300, 500)

class ListScreen(Screen):
    pass

class PlusScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(ListScreen(name='Lists'))
sm.add_widget(PlusScreen(name='Plus'))

class BootcampList(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = 'A700'
        screen = Builder.load_string(toolbar_helper)

        return screen

BootcampList().run()