def bottomNav_main(data, i, ncomponents):
    Ids = []
    bottomNav = data['combinedjson']['compos'][i]
    embeddedcompos = bottomNav.get('embeddedcompos')
    embeddedtext = bottomNav.get('embeddedtext')
    tabs = False
    icon_count = 0
    if (embeddedcompos):
        for j in range(len(embeddedcompos)):
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
        Ids.append(text_trunacate(embeddedtext))

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


def text_trunacate(embeddedtext):
    for i in range(len(embeddedtext)):
        if (embeddedtext[i]['text_content'] == embeddedtext[i]['text_meta']):
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
