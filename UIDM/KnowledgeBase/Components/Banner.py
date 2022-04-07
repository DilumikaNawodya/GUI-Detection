def banner_main(data, i, ncomponents):
    banner = data['combinedjson']['compos'][i]
    embeddedcompos = banner.get('embeddedcompos')
    embeddedtext = banner.get('embeddedtext')
    button = False
    btn_count = []
    btn_type = []
    if (embeddedcompos):
        for j in range(len(embeddedcompos)):
            if (embeddedcompos[j]['name'] == "Button"):
                button = True
                btn_count += [i]
                btn_type.append(embeddedcompos[j]['type'])
        banner_button(button, btn_count, btn_type)
        mismatch_btn_banner(banner, btn_type)
        banner_btn_order(btn_count, embeddedcompos)
        icon_w_text(embeddedcompos, embeddedtext)
        top_bar = -1
        for j in range(ncomponents):
            if data['combinedjson']['compos'][j]["name"] == "Appbar: Top":
                top_bar = j
                break
        top_bar_w_banner(top_bar, banner, data)

    # Call Functions
    banner_count(data, ncomponents)
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
        if ("contained" in btn_type or len(btn_count) == 1):
            return "Caution"
        if (len(btn_count) > 2):
            return "Error"
    return "Success"


def mismatch_btn_banner(banner, btn_type):
    if (banner):
        if (len(set(btn_type)) != 1 and "contained" in btn_type):
            return "Error"
    return "Success"


def banner_btn_order(btn_count, embeddedcompos):
    if (embeddedcompos[btn_count[0]]['position']['row_max'] == embeddedcompos[btn_count[1]]['position']['row_max']):
        return "Success"
    return "Caution"


def icon_w_text(embeddedcompos, embeddedtext):
    icon = False
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "Icon":
            icon = True
    if (icon):
        if (not embeddedtext):
            return "Error"
    return "Success"


def top_bar_w_banner(top_bar, banner, data, top_bar_bottom_edge, banner_top_edge):
    top_bar_bottom_edge = data['combinedjson']['compos'][top_bar]['position']['row_max']
    banner_top_edge = banner['position']['row_min']
    if (banner_top_edge > top_bar_bottom_edge):
        return "Error"
    return "Success"

##############################
### Color Detection Needed ###
##############################


# def btn_links(banner, link):
#     if (banner and link):
#         return "Error"
#     return "Success"

##############################
### Icon Detection Needed  ###
##############################

# def close_affordance(banner, close):
#     if (banner and close):
#         return "Error"
#     return "Success"
