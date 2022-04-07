def navdrawer_main(data, i, ncomponents, screen_size):
    NavDrawer = data['combinedjson']['compos'][i]
    embeddedcompos = NavDrawer.get('embeddedcompos')
    embeddedtext = NavDrawer.get('embeddedtext')
    textmeta = NavDrawer.get('textmeta')

    bottom_bar = False
    top_bar = False
    for j in range(ncomponents):
        if data['combinedjson']['compos'][i]["name"] == "Appbar: Bottom":
            bottom_bar = True
            break
        if data['combinedjson']['compos'][i]["name"] == "Appbar: Top":
            top_bar = True
            break

    if (embeddedcompos):
        nav_dest_count = 0
        for i in len(embeddedcompos):
            if embeddedcompos[i]['name'] == "Destination":
                nav_dest_count += 1
        # Call Functions
        nav_destinations(nav_dest_count)
        detect_dividers(embeddedcompos, nav_dest_count)
        branding_element(embeddedcompos, screen_size[0], NavDrawer['height'])
        branding_w_top_bar(
            embeddedcompos, screen_size[0], NavDrawer['height'], top_bar)
        bottom_drawer_size(NavDrawer, embeddedcompos)

    if (embeddedtext):
        text_wo_icons(embeddedtext)
        shrink_text(embeddedtext)
        if (textmeta):
            text_truncate(embeddedtext, textmeta, NavDrawer['width'])

    nav_components(bottom_bar)
    nav_drawer_side(NavDrawer, screen_size)

    return


def nav_destinations(count):
    if (count >= 5):
        return "Success"
    return "Error"


def nav_components(bottom_bar):
    if (bottom_bar == True):
        return "Caution"
    return "Success"


def nav_drawer_side(NavDrawer, screen_size):
    if (NavDrawer['width'] < screen_size[1]):
        return "Success"
    if (NavDrawer['height'] < screen_size[0]):
        return "Success"
    return "Error"


def text_wo_icons(embeddedtext):
    if (len(embeddedtext) > 1):
        return "Success"
    return "Error"


def text_truncate(embeddedtext, textmeta, draw_width):
    if (draw_width < len(textmeta)*4):
        if (textmeta != embeddedtext[0]['text_content']):
            return "Success"
    if (textmeta == embeddedtext[0]['text_content']):
        return "Success"
    return "Error"


def shrink_text(embeddedtext):
    regualr_text_size = embeddedtext[len(embeddedtext)/2]['height']
    for i in range(1, len(embeddedtext)-1):
        if (regualr_text_size == embeddedtext[i]['height']):
            return "Success"
    return "Error"


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
        return "Error"
    return "Success"

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
