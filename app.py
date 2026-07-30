from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image

class DoctorFrioApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=15)
        
        # 1. IMAGE
        layout.add_widget(Image(source="image.png", size_hint=(1, 0.25)))
        
        # 2. TITRE
        layout.add_widget(MDLabel(text="Doctor Frio", halign="center", font_style="H4"))
        
        # 3. CHAMPS
        layout.add_widget(MDTextField(hint_text="Nom"))
        layout.add_widget(MDTextField(hint_text="Téléphone"))
        
        # 4. BOUTON
        layout.add_widget(MDRaisedButton(text="Envoyer", pos_hint={"center_x": 0.5}))
        
        return layout

DoctorFrioApp().run()