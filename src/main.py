from taipy.gui import Gui, navigate


root="<|menu|label=Menu|lov={[('Page-1', 'Page 1'), ('Page-2', 'Page 2')]}|on_action=on_menu|>"
Home="## This is page 1"
Create="## This is page 2"


def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)


pages = {
    "/": root_md,
    "Page-1": Home,
    "Page-2": Create
}

Gui(pages=pages).run(dark_mode=False, use_reloader=True)