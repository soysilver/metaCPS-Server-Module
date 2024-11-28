from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock

import updater
import Server

import threading


'''
This file is the main function of the server program.
This is a seperate program, yet it communicates with CPS.
1. this part sets up tcp connection
2. also publiches the app -> prior to release, check https://kivy.org/doc/stable/guide/licensing.html
3. What each uses:
- ZMQ follows Modified BSD License -> not gonna use
- kivy follows MIT License
'''

class StartScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        label = Label(text="click to update database", size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.2, 'y': 0.85})
        self.add_widget(label)
        button = Button(text=" update\ndatabase", size_hint=(0.2, 0.15), pos_hint={'x': 0.7, 'y': 0.8})
        button.bind(on_press=self.press)      
        self.add_widget(button)
        
        
        self.start_thread()

    def press(self, instance):
        thread2 = threading.Thread(target=self.run_updater)
        thread2.start()

    def run_updater(self):
        updater.runFile()

    def start_thread(self):
        thread = threading.Thread(target=self.run_optimalOp)
        thread.daemon = True
        thread.start()


    def run_optimalOp(self):
        Server.start_server(port = 7777)



class myApp(App):
    def build(self):
 
        return StartScreen()

    
if __name__ == '__main__':
    Window.size = (400, 300) 
    myApp().run()
