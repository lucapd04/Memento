from taipy.gui import Gui, navigate
import cohere

# Lily cohere work here

root_pg="<|menu|label=Menu|lov={[('Home', 'Home'), ('Create', 'Create')]}|on_action=on_menu|>"

Home_pg='''
<h1>Home</h1>
'''
# Cohere page 
Create_pg='''
<h1>Create</h1>
'''


def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)


pages = {
    "/": root_pg,
    "Home": Home_pg,
    "Create": Create_pg
}

Gui(pages=pages).run(dark_mode=False, use_reloader=True)