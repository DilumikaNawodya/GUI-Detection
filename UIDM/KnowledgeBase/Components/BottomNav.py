def bottomNav_main(data, i, ncomponents):
    bottomNav = data['combinedjson']['compos'][i]
    embeddedcompos = bottomNav.get('embeddedcompos')
    embeddedtext = bottomNav.get('embeddedtext')
    icon = False
    tabs = False
    icon_count = 0
    if (embeddedcompos):
        for j in len(embeddedcompos):
            if (embeddedcompos[j]['name'] == "Icon"):
                icon = True
                icon_count += 1
            if (embeddedcompos[j]['name'] == "Tabs"):
                tabs = True
        # Call Functions
        n_destinations(icon_count)
        tabs_w_bottomnav(tabs, bottomNav)
    if (embeddedtext):
        text_size(embeddedtext)
        text_lines_banner(embeddedtext)
    return


def n_destinations(icon_count):
    if (icon_count < 3 or icon_count > 5):
        return "Error"
    return "Success"


def tabs_w_bottomnav(tabs, bottomnav):
    if (tabs and bottomnav):
        return "Caution"
    return "Error"


def text_size(embeddedtext):
    height = embeddedtext[0]['height']
    for i in range(1, len(embeddedtext)):
        if (embeddedtext[i]['height'] != height):
            return "Error"
    return "Success"


def text_lines_banner(embeddedtext):
    height = embeddedtext[0]['height']
    for i in range(1, len(embeddedtext)):
        if (embeddedtext[i]['height'] == height*2 or embeddedtext[i]['height'] == height//2):
            return "Caution"
    return "Success"


########################################
### Meta file data extraction needed ###
########################################

# def text_trunacate(text_meta, text_detect):
#     for i in len(text_detect):
#         text_detect[i] == text_meta[i]
#         return "Success"
#     return "Error"

##############################
### Color Detection Needed ###
##############################

# def destination_color(destination_colors):
#     color_set = set(destination_colors)
#     if (color_set > 2):
#         return "Error"
#     return "Success"
