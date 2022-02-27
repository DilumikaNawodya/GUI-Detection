def banner_main(data, i, ncomponents):
    banner = data['combinedjson']['compos'][i]
    embeddedcompos = banner['embeddedcompos']
    button = False
    btn_count = 0
    btn_type = []
    for j in range(len(embeddedcompos)):
        if (embeddedcompos[j]['name'] == "Button"):
            button = True
            btn_count += 1
            btn_type.append(embeddedcompos[j]['type'])

    # Call Functions
    banner_count(data, ncomponents)
    banner_button(button, btn_count, btn_type)
    mismatch_btn_banner(banner, btn_type)
    return


def banner_count(data, ncomponents):
    count = 0
    for j in range(ncomponents):
        if (data['combinedjson']['compos'][j]["name"] == "Banner"):
            count += 1
    if (count > 1):
        return "Error"
    return "Success"


def banner_button(button, btn_count, btn_type):
    if (button):
        if ("contained" in btn_type or btn_count == 1):
            return "Caution"
        if (btn_count > 2):
            return "Error"
    return "Success"


def mismatch_btn_banner(banner, btn_type):
    if (banner):
        if (len(set(btn_type))!=1 and "contained" in btn_type):
            return "Error"
    return "Success"


def banner_btn_order(btn1_bottom_edge, btn2_bottom_edge):
    if (btn1_bottom_edge == btn2_bottom_edge):
        return "Success"
    return "Caution"


def close_affordance(banner, close):
    if (banner and close):
        return "Error"
    return "Success"


def icon_w_text(icon, text):
    if (icon):
        if (not text):
            return "Error"
    return "Success"

# The surface containing a banner should be clearly distinguished from the top app bar surface.


def top_bar_w_banner(top_bar_bottom_edge, banner_top_edge):
    if (banner_top_edge > top_bar_bottom_edge):
        return "Error"
    return "Success"


def banner_count(banner_count):
    if (banner_count > 1):
        return "Success"
    return "Error"


##############################
### Color Detection Needed ###
##############################


# def btn_links(banner, link):
#     if (banner and link):
#         return "Error"
#     return "Success"
