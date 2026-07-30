from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class NouveauClientScreen(MDScreen):
    pass

class DoctorFrioApp(MDApp):
    def build(self):
        self.title = "Doctor Frio"
        self.theme_cls.primary_palette = "Blue"
        
        screen = MDScreen()
        
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=10)
        
        title = MDLabel(
            text="Nouveau Client",
            halign="center",
            font_style="H5"
        )
        
        btn = MDRaisedButton(
            text="Enregistrer",
            pos_hint={"center_x": 0.5}
        )
        
        layout.add_widget(title)
        layout.add_widget(btn)
        screen.add_widget(layout)
        return screen

if _name_ == '_main_':
    DoctorFrioApp().run()
