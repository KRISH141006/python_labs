from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.input = TextInput(font_size=30, size_hint=(1, 0.4))
        self.output = Label(text="", font_size=40)
        btn = Button(text="Show Text", font_size=30, size_hint=(1, 0.3))

        btn.bind(on_press=self.show_text)

        layout.add_widget(self.input)
        layout.add_widget(btn)
        layout.add_widget(self.output)

        return layout

    def show_text(self, instance):
        self.output.text = self.input.text

TextInputApp().run()
