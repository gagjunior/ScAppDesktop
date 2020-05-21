import kivy
from kivy.app import App
from telas.views import Gerenciador

kivy.require('1.11.1')


class ScApp(App):
    def build(self):
        self.title = 'Relatório de Serviço'
        return Gerenciador()


if __name__ == "__main__":
    ScApp().run()
    