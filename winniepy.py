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

  # add component: label
  def add_label(self, text:str):
    label = Label(self, text)
    self.components.append(label)
    return label

  # add component: textbox
  def add_textbox(self):
    textbox = TextBox(self)
    self.components.append(textbox)
    return textbox

  # make the window show on screen
  def show(self): self.root.mainloop()

class Component:
  # master: parent window
  def __init__(self, master:Window):
    self.master = master.root
    self.widget = None

  # appearance: changing background color
  def background_color(self, color:str=""):
    # if widget isn't None
    if self.widget:
      # if no new value provided, just return the current value
      if color != "": self.widget.config(bg=color)
      return self.widget.cget("bg")

  # appearance: changing foreground color
  def foreground_color(self, color:str=""):
    # if widget isn't None
    if self.widget:
      # if no new value provided, just return the current value
      if color != "": self.widget.config(fg=color)
      return self.widget.cget("fg")

  # applied on every components
  # placing component
  def place(self, x:int, y:int):
    if self.widget: self.widget.place(x=x,y=y)

class Button(Component):
  # create and add button to master
  def __init__(self, master:Window, text:str):
    super().__init__(master)
    self.widget = tk.Button(master.root, text=text)
    # default position
    self.place(0,0)

  # appearance: changing button's text
  def text(self, text:str=""):
    # if no new value provided, just return the current value
    if text != "": self.widget.config(text=text)
    return self.widget.cget("text")

  # events: button
  # on_click: left click
  def on_click(self, command=None):
    if command: self.widget.config(command=command)

class Label(Component):
  def __init__(self, master:Window, text:str):
    super().__init__(master)
    self.widget = tk.Label(master.root, text=text)
    # default position
    self.place(0,0)

  # appearance: changing button's text
  def text(self, text:str=""):
    # if no new value provided, just return the current value
    if text != "": self.widget.config(text=text)
    return self.widget.cget("text")

class TextBox(Component):
  def __init__(self, master:Window):
    super().__init__(master)
    # create value property and binnd with the textbox
    self.value = tk.StringVar()
    self.widget = tk.Entry(master.root, textvariable=self.value)
    # default position
    self.place(0,0)

  # get current text value
  def text(self, value:str=""):
    if value != "": self.value.set(value)
    return self.value.get()
