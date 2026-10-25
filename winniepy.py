import tkinter as tk

class Window:
  # initialization ofc
  def __init__(self, title:str, width:int, height:int):
    self.root = tk.Tk()
    self.root.title(title)
    self.root.geometry(f"{width}x{height}")
    # tracking components
    self.components = []

  # make the window show on screen
  def show(self): self.root.mainloop()
