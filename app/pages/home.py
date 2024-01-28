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
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* Creates three columns with equal width */
            gap: 10px; /* Adjust the gap between grid items */
        }

        .image {
            max-width: 100%;
            height: auto;
        }
    </style>

    <div class="grid-container">
        <input type="image" src="Images/image9.jpeg" name="jarName" class="image"/>
        <input type="image" src="Images/image8.jpeg" name="jarName" class="image"/>
        <input type="image" src="Images/image7.jpeg" name="jarName" class="image"/> 
    </div>

    <div class="middle">
        <div class="text">Jar</div>
        <input type="image" src="Images/white_arrow.png" name="saveForm" class="btTxt submit" id="switch-jar" />
    </div>
</div>
    UoftHacks 11!
    |>
    <|
<|Settings|button|>

<|Create a new group|button|>

<br />

<|Friends|button|>
    |>
|> 
'''