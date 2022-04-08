def navdrawer_main(data, i, ncomponents, screen_size):
    Ids = []
    NavDrawer = data['combinedjson']['compos'][i]
    embeddedcompos = NavDrawer.get('embeddedcompos')
    embeddedtext = NavDrawer.get('embeddedtext')
    textmeta = NavDrawer.get('textmeta')

    bottom_bar = False
    bottom_nav = False
    top_bar = False
    for j in range(ncomponents):
        if data['combinedjson']['compos'][i]["name"] == "Bottom Navigation":
            bottom_nav = True
            break
        if data['combinedjson']['compos'][i]["name"] == "Appbar: Top":
            top_bar = True
            break
        if data['combinedjson']['compos'][i]["name"] == "Appbar: Bottom":
            bottom_bar = True
            break

    if (embeddedcompos):
        nav_dest_count = 0
        for i in len(embeddedcompos):
            if embeddedcompos[i]['name'] == "Destination":
                nav_dest_count += 1
        # Call Functions
        Ids.append(nav_destinations(nav_dest_count))
        Ids.append(detect_dividers(embeddedcompos, nav_dest_count))
        Ids.append(branding_element(embeddedcompos,
                   screen_size[0], NavDrawer['height']))
        Ids.append(branding_w_top_bar(
            embeddedcompos, screen_size[0], NavDrawer['height'], top_bar))
        Ids.append(bottom_drawer_size(bottom_bar, NavDrawer, embeddedcompos))

    if (embeddedtext):
        Ids.append(text_wo_icons(embeddedtext))
        Ids.append(shrink_text(embeddedtext))
        if (textmeta):
            Ids.append(text_truncate(
                embeddedtext, textmeta, NavDrawer['width']))

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


def text_truncate(embeddedtext, textmeta, draw_width):
    if (draw_width < len(textmeta)*4):
        if (textmeta != embeddedtext[0]['text_content']):
            return -1
    if (textmeta == embeddedtext[0]['text_content']):
        return -1
    return 95


def shrink_text(embeddedtext):
    regualr_text_size = embeddedtext[len(embeddedtext)//2]['height']
    for i in range(1, len(embeddedtext)-1):
        if (regualr_text_size == embeddedtext[i]['height']):
            return -1
    return 97


def detect_dividers(embeddedcompos, nav_dest_count):
    divider_count = 0
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "Divider":
            divider_count += 1
    if (nav_dest_count > divider_count):
        return "Success"
    return "Error"


def branding_element(embeddedcompos, screen_height, drawer_height):
    branding = False
    if embeddedcompos[0]['height'] > embeddedcompos[1]['height']:
        branding = True
    if (screen_height > drawer_height):
        if (branding):
            return "Error"
    return "Success"


def branding_w_top_bar(embeddedcompos, screen_height, drawer_height, top_bar):
    branding = False
    if embeddedcompos[0]['height'] > embeddedcompos[1]['height']:
        branding = True
    if (top_bar == True and drawer_height < screen_height):
        if (branding == True and embeddedcompos[0]['position']['row_min'] < drawer_height):
            return "Success"
    return "Error"


def bottom_drawer_size(NavDrawer, embeddedcompos, item, item_size, drawer_height):
    if (NavDrawer['position']['row_max'] > embeddedcompos[-1]['position']['row_max']+embeddedcompos[-1]['height']):
        return 98
    return -1

###############################
### Icon recognition needed ###
###############################

# def icon_semantics(icon1, icon2):
#     if (icon1 == icon2):
#         return "Error"
#     return "Success"

# def account_switch(drawer_height, arrow_icon, arrow_loc):
#     if (arrow_icon == True):
#         if (arrow_loc < drawer_height/4):
#             return "Success"
#     return "Error"
