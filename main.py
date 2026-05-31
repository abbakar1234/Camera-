from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from plyer import camera
from threading import Thread
import time
import os

class CameraApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Enter number of photos")
        self.input = TextInput(hint_text="e.g 3", multiline=False)

        self.button = Button(text="Start Capture")
        self.button.bind(on_press=self.start)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.button)

        return self.layout

    def start(self, instance):
        Thread(target=self.capture).start()

    def capture(self):
        try:
            total = int(self.input.text)

            folder = "/storage/emulated/0/DCIM/MyCameraApp"
            if not os.path.exists(folder):
                os.makedirs(folder)

            for i in range(total):
                path = f"{folder}/photo_{i+1}.jpg"
                self.label.text = f"Taking photo {i+1}/{total}"
                camera.take_picture(filename=path)
                time.sleep(3)

            self.label.text = "Done ✔️ Saved!"

        except Exception as e:
            self.label.text = str(e)

CameraApp().run()
