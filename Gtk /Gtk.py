import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class App(Gtk.Window):
    def __init__(self):
        super().__init__(title= "Meu Primeiro APP Gtk")
        self.set_default_size(700, 500)
        self.Tela()
        self.Frames()
        self.Widgets()
    
    def Tela(self):
        self.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#1e3743"))

    def Frames(self):
        self.tela_principal = Gtk.Frame(label= "Tela_principal")
        self.add(self.tela_principal)

    def Widgets(self):
        self.bt_teste = Gtk.Button(label= "aperte aqui")
        self.bt_teste.set_size_request(120, 40)
        self.tela_principal.add(self.bt_teste)

app = App() 
app.connect("destroy", Gtk.main_quit) 
app.show_all() 
Gtk.main()