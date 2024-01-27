from taipy.gui import Gui, navigate
import cohere

create_pg = '''
<|menu|label=Menu|lov={page_names}|on_action=on_menu|>
Create
'''
