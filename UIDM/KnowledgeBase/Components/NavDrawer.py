def navdrawer_main(data, i, ncomponents, screen_size):
    NavDrawer = data['combinedjson']['compos'][i]
    embeddedcompos = NavDrawer['embeddedcompos']
    embeddedtext = NavDrawer['embeddedtext']
    textmeta = NavDrawer['textmeta']

    nav_dest_count = 0
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "Destination":
            nav_dest_count += 1

    bottom_bar = False
    for j in range(ncomponents):
        if data['combinedjson']['compos'][i]["name"] == "Appbar: Bottom":
            bottom_bar = True

    # Call Functions
    nav_destinations(nav_dest_count)
    nav_components(bottom_bar)
    nav_drawer_side(NavDrawer, screen_size)
    text_wo_icons(embeddedtext)
    text_truncate(embeddedtext, textmeta, NavDrawer['width'])
    wrap_label(embeddedtext)
    return


def nav_destinations(count):
    if (count >= 5):
        return "Success"
    return "Error"


def nav_components(bottom_bar):
    if (bottom_bar == True):
        return "Caution"
    return "Success"

# rigt to left lanugage vs left to right language


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


def wrap_label(embeddedtext):
    text_lines = embeddedtext[len(embeddedtext)/2]['height']
    if (text_lines == 1):
        return "Success"
    return "Error"


def shrink_text(embeddedtext, regualr_text_size, text_size):
    regualr_text_size = embeddedtext[len(embeddedtext)/2]['height']
    if (regualr_text_size == text_size):
        return "Success"
    return "Error"


def icon_semantics(icon1, icon2):
    if (icon1 == icon2):
        return "Error"
    return "Success"

# Secondary destinations can be represented by the same icon, especially if they are part of a collection (1)


def icons_w_texts(icon, text):
    if (len(icon) == len(text)):
        return "Success"
    return "Error"


def detect_dividers(divider_count, destination_count):
    if (destination_count > divider_count):
        return "Success"
    return "Error"


def account_switch(drawer_height, arrow_icon, arrow_loc):
    if (arrow_icon == True):
        if (arrow_loc < drawer_height/4):
            return "Success"
    return "Error"


def branding_element(screen_height, drawer_height, branding):
    if (screen_height > drawer_height):
        if (branding):
            return "Error"
    return "Success"


def branding_w_top_bar(top_bar, drawer_height, screen_height, branding, branding_loc):
    if (top_bar == True and drawer_height < screen_height):
        if (branding == True and branding_loc > drawer_height):
            return "Success"
    return "Error"

# A modal drawer is always opened by a navigation menu icon (1).


def bottom_drawer_size(item, item_size, drawer_height):
    if (drawer_height > item_size*item+10):
        return "Error"
    return "Success"

# Adjust the opening position of your bottom navigation drawer so the last list item in view is clipped by the bottom of the screen. This can inform users that there are more items to view.


def landscape_bottom_drawer(mode, screen_height, drawer_height):
    if (mode == "landscape"):
        if (screen_height/2 == drawer_height):
            return "Error"
    return "Success"

# Scrolling option

# def one_active_drawer()
