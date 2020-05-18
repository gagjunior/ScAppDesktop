from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.core.window import Window
import os

dir_name = os.path.dirname(__file__)

Builder.load_string(open(f'{dir_name}/login.kv', encoding='utf-8').read())
class Login(Screen):
    def tela_cadastro(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'cadastro'    


Builder.load_string(open(f'{dir_name}/cadastro.kv', encoding='utf-8').read())
class Cadastro(Screen):
    def on_pre_enter(self, *args):
        Window.set_title('ScApp - Cadastro de Usuário')


class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super(Gerenciador, self).__init__(**kwargs)
        self.add_widget(Login(name='login'))
        self.add_widget(Cadastro(name='cadastro'))  










