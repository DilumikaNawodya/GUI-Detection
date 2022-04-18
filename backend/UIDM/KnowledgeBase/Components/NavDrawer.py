def navdrawer_main(data, i, ncomponents, screen_size):
    Ids = []
    NavDrawer = data['combinedjson']['compos'][i]
    embeddedcompos = NavDrawer.get('embeddedcompos')
    embeddedtext = NavDrawer.get('embeddedtext')

    bottom_bar = False
    bottom_nav = False
    top_bar = False
    for j in range(ncomponents):
        if data['combinedjson']['compos'][j]["name"] == "Bottom Navigation":
            bottom_nav = True
        if data['combinedjson']['compos'][j]["name"] == "Appbar: Top":
            top_bar = True
        if data['combinedjson']['compos'][j]["name"] == "Appbar: Bottom":
            bottom_bar = True

    if (embeddedcompos):
        nav_dest_count = 0
        for i in range(len(embeddedcompos)):
            if embeddedcompos[i]['name'] == "Destination":
                nav_dest_count += 1
        # Call Functions
        Ids.append(nav_destinations(nav_dest_count))
        Ids.append(detect_dividers(embeddedcompos, nav_dest_count))
        Ids.append(bottom_drawer_size(NavDrawer, embeddedcompos))

    if (embeddedtext):
        Ids.append(text_wo_icons(embeddedtext))
        Ids.append(shrink_text(embeddedtext))
        Ids.append(text_truncate(
            embeddedtext))

    Ids.append(nav_components(bottom_nav))
    Ids.append(nav_drawer_side(bottom_bar, NavDrawer, screen_size))

    return Ids


def nav_destinations(count):
    if (count >= 5):
        return -1
    return 90


def nav_components(bottom_nav):
    if (bottom_nav == True):
        return 91
    return -1


def nav_drawer_side(bottom_bar, NavDrawer, screen_size):
    if (NavDrawer['width'] < screen_size[1]):
        return -1
    if (bottom_bar):
        if (NavDrawer['height'] < screen_size[0]):
            return -1
    return 92


def text_wo_icons(embeddedtext):
    if (len(embeddedtext) > 1):
        return -1
    return 94


def text_truncate(embeddedtext):
    for i in range(len(embeddedtext)):
        if (embeddedtext[i]['text_meta'] != embeddedtext[i]['text_content']):
            return 95
    return -1


def shrink_text(embeddedtext):
    regualr_text_size = embeddedtext[len(embeddedtext)//2]['height']
    for i in range(1, len(embeddedtext)-1):
        if (regualr_text_size == embeddedtext[i]['height']):
            return -1
    return 97


def detect_dividers(embeddedcompos, nav_dest_count):
    divider_count = 0
    for i in range(len(embeddedcompos)):
        if embeddedcompos[i]['name'] == "Divider":
            divider_count += 1
    if (divider_count != 0 and nav_dest_count > divider_count):
        return 100
    return -1


def bottom_drawer_size(NavDrawer, embeddedcompos):
    if (NavDrawer['position']['row_max'] > embeddedcompos[len(embeddedcompos)-1]['position']['row_max']+embeddedcompos[len(embeddedcompos)-1]['height']):
        return 98
    return -1
