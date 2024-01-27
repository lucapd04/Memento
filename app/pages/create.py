from taipy.gui import Gui, navigate, Markdown
import cohere
import json
import numpy as np
 

#cohere component
co = cohere.Client('90lG7PeJDEJgf4pWS0ObCcS57x97XaUwh15g2U7Z')

# Read JSON file
with open('./app/data.json', 'r') as file:
    data = json.load(file)

# Combine all image descriptions
combined_description = ", ".join(image_info.get('description', '') for image_info in data.get('images', []))

#

response = co.chat(
    message="Tell a story using these image descriptions in choronological order: number each description and output with image number"+combined_description
    
)

print(response)
path_upload=""

create_pg = '''
<|menu|label=Menu|lov={page_names}|on_action=on_menu|>

<|{"../memento.svg"}|image|width=0.1|>

<|text-center|
<|{path_upload}|file_selector|extensions=.png,.jpg|label=Upload image|>
<|{path_upload}|image|>
<|{dt}|not with_time|date|>
<|{memories}|label=Memory associated with image?|multiline=True|lines= 5|action_keys="Enter"|input|>

<|{response.text}|text|>
>
'''