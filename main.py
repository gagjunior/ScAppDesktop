import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from telas.views import Login, Cadastro

kivy.require('1.11.1')

gerenciador = ScreenManager()
gerenciador.add_widget(Login(name='login'))
gerenciador.add_widget(Cadastro(name='cadastro'))



class ScApp(App):
    def build(self):
        self.title = 'Relatório de Serviço'
        return gerenciador



if __name__ == "__main__":
    ScApp().run()
    