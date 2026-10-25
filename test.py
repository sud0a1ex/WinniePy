from winniepy import *

def greet(): print("Hello there!")
app = Window("Hello, world!", 800, 600)
btn1 = app.add_button("Click Me!")
btn1.on_click(greet)
app.show()
