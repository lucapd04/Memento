from taipy.gui import Gui, navigate, Markdown
import cohere
import numpy as np

co = cohere.Client('90lG7PeJDEJgf4pWS0ObCcS57x97XaUwh15g2U7Z')

path_upload=""
dt=""
memories=""
img=""

def on_change(state, var_name, var_val):
  if var_name == "memories":
    state.memories = var_val
    
  if var_name == "path_upload":
    state.img = var_val

def button_pressed(state):
  
  # error msg
  if state.memories == "":
    notify()

  response = co.chat(
    chat_history=[
    {
        "role": 
        "USER", "message": 
        "Make a story with a lot of emotions with the following memories: I ate ice cream with my friends today and my friend got ice cream all over their face we also rollerbladed and my friend fell many times "
        },
    {
        "role": 
        "CHATBOT", 
        "message": 
        "On this day, you and your friends went on an adventure. It began with shared ice cream, leaving stains on your face that left you all giggling. Then turning into rollerblading gliding through the park. You stumbled and fell, and your friend after some laugher lifted you up."
        }
  ],
    message="Tell a story using these image descriptions in choronological order: number each description and output with image number"+combined_description

)

create_pg = '''
<|menu|label=Menu|lov={page_names}|on_action=on_menu|>

<|{"../memento.svg"}|image|width=0.1|>
<|toggle|theme|>

<|text-center|
<|{path_upload}|file_selector|extensions=.png,.jpg|label=Upload image|>
<|{dt}|not with_time|date|>
<|{memories}|label=Memory associated with image?|multiline=True|lines= 5|action_keys="Enter"|on_change=get_memories|input|>

<|{path_upload}|image|>

<|{"Submit"}|button|on_action=button_pressed|>
>
'''