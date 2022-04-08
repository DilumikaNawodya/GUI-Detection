def bottomNav_main(data, i, ncomponents):
    Ids = []
    bottomNav = data['combinedjson']['compos'][i]
    embeddedcompos = bottomNav.get('embeddedcompos')
    embeddedtext = bottomNav.get('embeddedtext')
    text_meta = bottomNav.get('textmeta')
    tabs = False
    icon_count = 0
    if (embeddedcompos):
        for j in len(embeddedcompos):
            if (embeddedcompos[j]['name'] == "Icon"):
                icon_count += 1
            if (embeddedcompos[j]['name'] == "Tabs"):
                tabs = True
        # Call Functions
        Ids.append(n_destinations(icon_count))
        Ids.append(tabs_w_bottomnav(tabs, bottomNav))
    if (embeddedtext):
        Ids.append(text_size(embeddedtext))
        Ids.append(text_lines_banner(embeddedtext))
        if (text_meta):
            Ids.append(text_trunacate(text_meta, embeddedtext))
    return Ids


def n_destinations(icon_count):
    if (icon_count < 3):
        return 48
    if (icon_count > 5):
        return 49
    return -1


def tabs_w_bottomnav(tabs, bottomnav):
    if (tabs and bottomnav):
        return 50
    return -1


def text_trunacate(text_meta, embeddedtext):
    for i in len(embeddedtext):
        embeddedtext[i]['text_content'] == text_meta[i]
        return -1
    return 52


def text_size(embeddedtext):
    height = embeddedtext[0]['height']
    for i in range(1, len(embeddedtext)):
        if (embeddedtext[i]['height'] != height):
            return 53
    return -1


def text_lines_banner(embeddedtext):
    height = embeddedtext[0]['height']
    for i in range(1, len(embeddedtext)):
        if (embeddedtext[i]['height'] == height*2 or embeddedtext[i]['height'] == height//2):
            return 54
    return -1


##############################
### Color Detection Needed ###
##############################

# def destination_color(destination_colors):
#     color_set = set(destination_colors)
#     if (color_set > 2):
#         return "Error"
#     return "Success"
