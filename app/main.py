from taipy.gui import Gui, navigate
from pages.home import *
from pages.create import *

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)

pages = {
    "/": "<|menu|label=Menu|lov={page_names}|on_action=on_menu|>",
    "Home": home_pg,
    "Create": create_pg,
}

page_names = [page for page in pages.keys() if page != "/"]

Gui(pages=pages).run(dark_mode=False, use_reloader=True, port=5001)