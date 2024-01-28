from taipy.gui import Gui, navigate
# sidebar = '''
# <|Settings|button|>
# '''

home_pg = '''
<|{"../images/logo.svg"}|image|width=0.1|>
<|toggle|theme|>
<|menu|label=Menu|lov={page_names}|on_action=on_menu|>
#Home {: .header }
<|layout|columns = 1 1|
    <|
<div class="container" style="background-color: grey;">

    <input type="image" src="Images/image9.jpeg" name="jarName" class="image"/>
    <div class="middle">
        <div class="text">Jar</div>
        <input type="image" src="Images/white_arrow.png" name="saveForm" class="btTxt submit" id="switch-jar" />
    </div>
</div>
    insert description here
    |>
    <|
<|Settings|button|>

<br />

<|Create a new group|button|>

<br />

<|Friends|button|>
    |>
|> 
'''

