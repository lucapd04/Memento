from taipy.gui import Gui, navigate
# sidebar = '''
# <|Settings|button|>
# '''

home_pg = '''
<|{"../memento.svg"}|image|width=0.1|>
<|menu|label=Menu|lov={page_names}|on_action=on_menu|>
#Home {: .header }
<|layout|columns = 1 1|
    <|
<button class="custom-button">Jar</button>
<input type="image" src="Images/R.png" name="saveForm" class="btTxt submit" id="switch-jar" />
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