import tkinter as tk

class Window:
  # initialization ofc
  def __init__(self, title:str, width:int, height:int):
    self.root = tk.Tk()
    self.root.title(title)
    self.root.geometry(f"{width}x{height}")
    # tracking components
    self.components = []

  # add component: button
  def add_button(self, text:str):
    button = Button(self, text)
    self.components.append(button)
    return button

  # make the window show on screen
  def show(self): self.root.mainloop()

class Component:
  # master: parent window
  def __init__(self, master:Window):
    self.master = master.root
    self.widget = None

  # placing component
  def place(self, x:int, y:int):
    if self.widget: self.widget.place(x=x,y=y)

class Button(Component):
  # create and add button to master
  def __init__(self, master:Window, text):
    super().__init__(master)
    self.widget = tk.Button(master.root, text=text)

  # config: changing background color
  def background_color(self, color:str=""):
    # if no new value provided, just return the current value
    if color != "": self.widget.config(bg=color)
    return self.widget.cget("bg")

  # config: changing foreground color
  def foreground_color(self, color:str=""):
    # if no new value provided, just return the current value
    if color != "": self.widget.config(fg=color)
    return self.widget.cget("fg")

  # config: changing button's text
  def text(self, text:str=""):
    # if no new value provided, just return the current value
    if text != "": self.widget.config(text=text)
    return self.widget.cget("text")
