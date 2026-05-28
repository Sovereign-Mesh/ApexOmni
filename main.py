from kivy.app import App
from kivy.uix.label import Label
class ApexOmniApp(App):
    def build(self):
        return Label(text="APEX OMNI: MESH CONTROL ONLINE")
if __name__ == '__main__':
    ApexOmniApp().run()
