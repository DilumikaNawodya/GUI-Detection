from .Components.Banner import banner_main
from .Components.BottomAppBar import bottomappbar_main
from .Components.BottomNav import bottomNav_main
from .Components.Button import button_main
from .Components.Cards import cards_main
from .Components.Dialogs import dialogs_main
from .Components.FAB import fab_main
from .Components.Lists import lists_main
from .Components.NavDrawer import navdrawer_main
from .Components.Tabs import tabs_main
from .Components.TextFields import textfield_main
from .Components.TopAppBar import topappbar_main


def divert(data):
    Ids = []
    ncomponents = len(data['combinedjson']['compos'])
    screen_size = [data['combinedjson']['screen_size']
                   [0], data['combinedjson']['screen_size'][1]]
    screen_size
    for i in range(ncomponents):
        name = data['combinedjson']['compos'][i]["name"]
        if (name == "Banner"):
            Ids += banner_main(data, i, ncomponents)
            break
        elif (name == "Appbar: Bottom"):
            Ids += bottomappbar_main(data, i, ncomponents)
            break
        elif (name == "Bottom Navigation"):
            Ids += bottomNav_main(data, i, ncomponents)
            break
        elif (name == "Button"):
            Ids += button_main(data, i, ncomponents)
            break
        elif (name == "Cards"):
            Ids += cards_main(data, i, ncomponents)
            break
        elif (name == "Dialogs"):
            Ids += dialogs_main(data, i, ncomponents)
            break
        elif (name == "Floating Action Button"):
            Ids += fab_main(data, i, ncomponents)
            break
        elif (name == "Lists"):
            Ids += lists_main(data, i, ncomponents, screen_size)
            break
        elif (name == "Navigation Drawer"):
            Ids += navdrawer_main(data, i, ncomponents, screen_size)
            break
        elif (name == "Tabs"):
            Ids += tabs_main(data, i, ncomponents)
            break
        elif (name == "Text Fields"):
            Ids += textfield_main(data, i, ncomponents)
            break
        elif (name == "Appbar: Top"):
            Ids += topappbar_main(data, i, ncomponents)
            break
    return Ids
