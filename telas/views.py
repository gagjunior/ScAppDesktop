from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
import os

dir_name = os.path.dirname(__file__)

Builder.load_string(open(f'{dir_name}/login.kv', encoding='utf-8').read())
class Login(Screen):
    pass
                
        


Builder.load_string(open(f'{dir_name}/cadastro.kv', encoding='utf-8').read())
class Cadastro(Screen):
    def on_pre_enter(self, *args):
        Window.set_title('ScApp - Cadastro')





