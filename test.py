from winniepy import *

app = Window("Hello, world!", 800, 600)
tb1 = app.add_textbox()
def greet():
  print(f"Yo, {tb1.text()}.")
btn1 = app.add_button("Click Me!")
btn1.on_click(greet)
btn1.place(0,20)
app.show()
