from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.count = 0

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text=str(self.count), font_size=60)
        btn = Button(text="Increment", font_size=40, size_hint=(1, 0.4))
        btn.bind(on_press=self.increment)

        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def increment(self, instance):
        self.count += 1
        self.label.text = str(self.count)

CounterApp().run()
