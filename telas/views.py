from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, SlideTransition
from kivy.core.window import Window
from kivy.clock import Clock
import os

dir_name = os.path.dirname(__file__)

# Tela Splash
Builder.load_string(open(f'{dir_name}/splash.kv', encoding='utf-8').read())
class Splash(Screen):
    def tela_login(self, *args):
        Window.borderless = False               
        self.manager.transition = FadeTransition()
        self.manager.current = 'login'
        
    def on_enter(self, *args):
        Clock.schedule_once(self.tela_login, 2)

    def on_pre_enter(self, *args):
        Window.borderless = True

    

# Tela Login
Builder.load_string(open(f'{dir_name}/login.kv', encoding='utf-8').read())
class Login(Screen):
    def tela_cadastro(self):
        self.manager.transition = SlideTransition()      
        self.manager.current = 'cadastro'

    def tela_menu(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'menu_inicio'


# Tela Cadastro
Builder.load_string(open(f'{dir_name}/cadastro.kv', encoding='utf-8').read())
class Cadastro(Screen):
    def on_pre_enter(self, *args):
        Window.set_title('ScApp - Cadastro de Usuário')
    
    def tela_login(self):
        self.manager.transition = SlideTransition()
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'


Builder.load_string(open(f'{dir_name}/menu.kv', encoding='utf-8').read())
class MenuInicio(Screen):
    def on_pre_enter(self, *args):
        Window.set_title('ScApp - Menu')


# Gerenciador de Telas
class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super(Gerenciador, self).__init__(**kwargs)
        self.add_widget(Splash(name='splash'))
        self.add_widget(Login(name='login'))
        self.add_widget(Cadastro(name='cadastro'))
        self.add_widget(MenuInicio(name='menu_inicio'))