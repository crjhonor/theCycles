import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
style = ttk.Style()
theme_names = style.theme_names()
theme_selection = ttk.Frame(root, padding=(10, 10, 10, 0))
theme_selection.pack(fill=X, expand=True)
lbl = ttk.Label(theme_selection, text="Select the theme")

theme_cbo = ttk.Combobox(
    master=theme_selection,
    text=style.theme.name,
    values=theme_names,
)
theme_cbo.pack(padx=10, side=RIGHT)
theme_cbo.current(theme_names.index(style.theme.name))

lbl.pack(side=RIGHT)

theme_selected = ttk.Label(
    master=theme_selection,
    text="litera",
    font="-size 24 -weight bold"
)
theme_selected.pack(side=LEFT)

def change_theme(event):
    theme_cbo_value = theme_cbo.get()
    style.theme_use(theme_cbo_value)
    theme_selected.configure(text=theme_cbo_value)
    theme_cbo.selection_clear()

theme_cbo.bind('<<ComboboxSelected>>', change_theme)

root.mainloop()