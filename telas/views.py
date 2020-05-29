from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, SlideTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import os

dir_name = os.path.dirname(__file__)

Builder.load_string(open(f'{dir_name}/splash.kv', encoding='utf-8').read())
Builder.load_string(open(f'{dir_name}/login.kv', encoding='utf-8').read())
Builder.load_string(open(f'{dir_name}/cadastro.kv', encoding='utf-8').read())
Builder.load_string(open(f'{dir_name}/menu.kv', encoding='utf-8').read())
Builder.load_string(open(f'{dir_name}/nova_atividade.kv', encoding='utf-8').read())


# Tela splash
class Splash(Screen):
    def inicio(self, *args):
        Window.borderless = False               
        self.manager.transition = FadeTransition()
        self.manager.current = 'login'
        
    def on_enter(self, *args):
        Clock.schedule_once(self.inicio, 2)

    def on_pre_enter(self, *args):
        Window.borderless = True


# Tela Login
class Login(Screen):
    pass    


# Tela Cadastro
class Cadastro(Screen):
    def on_pre_enter(self, *args):
        Window.set_title('ScApp - Cadastro de Usuário')


# Tela de menu inicial
class MenuInicio(Screen):
    def on_pre_enter(self, *args):
        Window.set_title('ScApp - Menu')



# Tela Nova atividade
class NovaAtividade(Screen):
    txt_pub = ObjectProperty()
    def on_pre_enter(self, *args):
        Window.set_title('ScApp - Nova Atividade')

    def adicionarPub(self):
        self.txt_pub.text = str("1")


# Gerenciador de Telas
class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super(Gerenciador, self).__init__(**kwargs)
        self.add_widget(Splash(name='splash'))
        self.add_widget(Login(name='login'))
        self.add_widget(Cadastro(name='cadastro'))
        self.add_widget(MenuInicio(name='menu_inicio'))
        self.add_widget(NovaAtividade(name='nova_atividade'))

    def tela_login(self, *args):                    
        self.transition = SlideTransition()
        self.transition.direction = 'right'
        self.current = 'login'
        
    def tela_cadastro(self):
        self.transition = SlideTransition()      
        self.current = 'cadastro'

    def tela_menu(self):
        self.transition = FadeTransition()
        self.current = 'menu_inicio'

    def tela_nova_atividade(self):
        self.transition = SlideTransition()
        self.current = 'nova_atividade'

        



        