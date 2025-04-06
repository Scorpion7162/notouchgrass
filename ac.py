import keyboard
import time
import threading
from pynput.mouse import Controller, Button

class AutoClicker:
    def __init__(self, cps=30):
        self.cps = cps
        self.running = False
        self.mouse = Controller()
        self.click_thread = None
        
    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()
            
    def start(self):
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self.clicking)
            self.click_thread.daemon = True
            self.click_thread.start()
            print("Press x to stop autoclicker")
            
    def stop(self):
        if self.running:
            self.running = False
            if self.click_thread and self.click_thread.is_alive():
                self.click_thread.join(timeout=1.0)
            print("Autoclicker stopped!")
    
    def clicking(self):
        sleep_time = 1.0 / self.cps
        
        while self.running:
            self.mouse.click(Button.left)
            time.sleep(sleep_time)

def main():
    clicker = AutoClicker(cps=30)
    print("Press Z to toggle click :o")
    print("Press esc to exit autoclicker")
    keyboard.add_hotkey('z', clicker.toggle)
    keyboard.wait('esc')
    clicker.stop()
    print("Program Closed")

if __name__ == "__main__":
    main()