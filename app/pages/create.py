from taipy.gui import Gui, navigate, Markdown
import cohere
import json




memories =""

create_pg = '''
<|menu|label=Menu|lov={page_names}|on_action=on_menu|>
<|{"../memento.svg"}|image|width=0.1|>

<|{path_upload}|file_selector|on_action=save_to_db|extensions=.png,.jpg|label=Upload image|>
<|{datetime}|not with_time|date|>
<|{""}|label=What memory is associated with this image?|multiline=True|lines= 5|action_keys="Enter"|input|>


def save_to_db(state):
    image = Image.open(state.path_upload)
    print(image)
    


'''
