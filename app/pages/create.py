from taipy.gui import Gui, navigate, Markdown
import cohere
import numpy as np

#cohere component
co = cohere.Client('90lG7PeJDEJgf4pWS0ObCcS57x97XaUwh15g2U7Z')

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
  message="Make a less superficial story with emotion with the following memories: I played video games with my friends all night and we tried over and over again just to win by the time we won we decided to meet up and eat a late night snack at mcdonalds "
)
print(response)

memories =""

create_pg = '''
<|{""}|label= add image|drop_message= "drop here to upload"|file_selector|>
<|{datetime}|not with_time|date|>
<|{""}|label=What memory is associated with this image?|multiline=True|lines= 5|action_keys="Enter"|input|>
'''
