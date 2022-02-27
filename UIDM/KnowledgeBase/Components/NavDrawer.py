def navdrawer_main(data, i, ncomponents):
    # Call Functions
    return


def nav_destinations(nav, count):
    if (nav == True and count >= 5):
        return "Success"
    return "Error"


def nav_components(nav_draw, bottom_bar):
    if (nav_draw == True and bottom_bar == True):
        return "Caution"
    return "Success"

# rigt to left lanugage vs left to right language


def nav_drawer_side(draw_left_edge, screen_left_edge, draw_top_edge, screen_top_edge):
    if (draw_left_edge < screen_left_edge):
        return "Success"
    if (draw_top_edge < screen_top_edge):
        return "Success"
    return "Error"


def text_wo_icons(texts):
    if (texts == True):
        return "Success"
    return "Error"


def text_truncate(text_meta, text_detect, draw_width):
    if (draw_width < len(text_meta)*4):
        if (text_meta != text_detect):
            return "Success"
    if (text_meta == text_detect):
        return "Success"
    return "Error"


def wrap_label(text_lines, regualr_text_size, text_size):
    if (text_lines == 1):
        return "Success"
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
