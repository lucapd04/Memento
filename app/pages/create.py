from taipy.gui import Gui, navigate, Markdown
import cohere
import json

# Cohere component
co = cohere.Client('90lG7PeJDEJgf4pWS0ObCcS57x97XaUwh15g2U7Z')

# Read JSON file
with open('./app/data.json', 'r') as file:
    data = json.load(file)

# Combine all image descriptions
combined_description = ", ".join(image_info.get('description', '') for image_info in data.get('images', []))

#

response = co.chat(
    message="Tell a story using these image description in choronological order"+combined_description
    
)

print("Combined Image Descriptions:")
print(combined_description)
print("\nCohere Response:")
print(response)




memories =""

create_pg = '''
<|{"../memento.svg"}|image|width=0.1|>

<|{path_upload}|file_selector|on_action=save_to_db|extensions=.png,.jpg|label=Upload image|>
<|{datetime}|not with_time|date|>
<|{""}|label=What memory is associated with this image?|multiline=True|lines= 5|action_keys="Enter"|input|>


def save_to_db(state):
    image = Image.open(state.path_upload)
    print(image)
    


'''
