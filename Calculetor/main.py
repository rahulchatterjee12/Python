import kivy 
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Calculetorlayout(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class CalculetorApp(App):
    def build(self):
        return Calculetorlayout()
    
calcApp = CalculetorApp()
calcApp.run()