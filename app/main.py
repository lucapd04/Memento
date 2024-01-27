from taipy.gui import Gui, navigate
from pages.home import home_pg
from pages.create import create_pg

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

pages = {
    "/": "<|menu|label=Menu|lov={[('Home', 'Home'), ('Create', 'Create')]}|on_action=on_menu|>",
    "Home": home_pg,
    "Create": create_pg
}

Gui(pages=pages).run(dark_mode=False, use_reloader=True)