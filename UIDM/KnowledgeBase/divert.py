import json
from Components.Banner import banner_main
from Components.BottomAppBar import bottomappbar_main
from Components.BottomNav import bottomNav_main
from Components.Button import button_main
from Components.Cards import cards_main
from Components.Dialogs import dialogs_main
from Components.FAB import fab_main
from Components.Lists import lists_main
from Components.NavDrawer import navdrawer_main
from Components.Tabs import tabs_main
from Components.TextFields import textfield_main
from Components.TopAppBar import topappbar_main

f = open('data.json')
data = json.load(f)

ncomponents = len(data['combinedjson']['compos'])
screen_size = [data['combinedjson']['img_shape']
               [0], data['combinedjson']['img_shape'][1]]

for i in range(ncomponents):
    name = data['combinedjson']['compos'][i]["name"]
    if (name == "Banner"):
        banner_main(data, i, ncomponents)
        break
    elif (name == "Appbar: Bottom"):
        bottomappbar_main(data, i, ncomponents)
        break
    elif (name == "Bottom Navigation"):
        bottomNav_main(data, i, ncomponents)
        break
    elif (name == "Button"):
        button_main(data, i, ncomponents)
        break
    elif (name == "Cards"):
        cards_main(data, i, ncomponents)
        break
    elif (name == "Dialogs"):
        dialogs_main(data, i, ncomponents)
        break
    elif (name == "Floating Action Button"):
        fab_main(data, i, ncomponents)
        break
    elif (name == "Lists"):
        lists_main(data, i, ncomponents)
        break
    elif (name == "Navigation Drawer"):
        navdrawer_main(data, i, ncomponents)
        break
    elif (name == "Tabs"):
        tabs_main(data, i, ncomponents)
        break
    elif (name == "Text Field"):
        textfield_main(data, i, ncomponents)
        break
    elif (name == "Appbar: Top"):
        topappbar_main(data, i, ncomponents)
        break
