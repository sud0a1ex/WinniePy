import tkinter as tk

DEFAULT_WINDOW_BACKGROUND = "#111522"
DEFAULT_FOREGROUND = "#dce3ef"
DEFAULT_BUTTON_BACKGROUND = "#1e263b"
DEFAULT_TEXTBOX_BACKGROUND = "#303d59"
DEFAULT_FRAME_COLOR = "#536684"

class Container:
  # initialization
  def __init__(self):
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

  # add component: frame
  def add_frame(self):
    frame = Frame(self)
    self.components.append(frame)
    return frame

class Window(Container):
  # initialization ofc
  def __init__(self, title:str, width:int, height:int):
    super().__init__()
    self.root = tk.Tk()
    self.root.title(title)
    self.root.geometry(f"{width}x{height}")
    # set default colors
    self.root.tk_setPalette(background=DEFAULT_WINDOW_BACKGROUND, foreground=DEFAULT_FOREGROUND)

  # make the window show on screen
  def show(self): self.root.mainloop()

class Component:
  # master: parent window
  def __init__(self, master):
    self.master = master.root if hasattr(master, "root") else master.widget
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
  def __init__(self, master, text:str):
    super().__init__(master)
    self.widget = tk.Button(self.master, text=text)
    # default position
    self.place(0,0)
    # set default color
    self.widget.config(bg=DEFAULT_BUTTON_BACKGROUND)

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
  def __init__(self, master, text:str):
    super().__init__(master)
    self.widget = tk.Label(self.master, text=text)
    # default position
    self.place(0,0)

  # appearance: changing button's text
  def text(self, text:str=""):
    # if no new value provided, just return the current value
    if text != "": self.widget.config(text=text)
    return self.widget.cget("text")

class TextBox(Component):
  def __init__(self, master):
    super().__init__(master)
    # create value property and binnd with the textbox
    self.value = tk.StringVar()
    self.widget = tk.Entry(self.master, textvariable=self.value)
    # default position
    self.place(0,0)
    # set default color
    self.widget.config(bg=DEFAULT_TEXTBOX_BACKGROUND)

  # get current text value
  def text(self, value:str|None = None):
    if value is not None: self.value.set(value)
    return self.value.get()

class Frame(Component, Container):
  def __init__(self, master):
    # initialize with self.master and self.components
    Component.__init__(self, master)
    Container.__init__(self)
    self.widget = tk.Frame(self.master)
    # default position
    self.place(0,0)
    # set default color
    self.widget.config(bg=DEFAULT_FRAME_COLOR)
