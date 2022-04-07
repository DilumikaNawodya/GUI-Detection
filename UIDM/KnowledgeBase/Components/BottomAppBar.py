def bottomappbar_main(data, i, ncomponents):
    bottomappbar = data['combinedjson']['compos'][i]
    embeddedcompos = bottomappbar.get('embeddedcompos')
    bar_top_edge = bottomappbar['position']['column_min']
    if (embeddedcompos):
        FAB = False
        keyboard = False
        snackbar = False
        for j in len(embeddedcompos):
            if (embeddedcompos[j]['name'] == "Floating Action Button"):
                FAB = True
                FAB_top_edge = embeddedcompos[j]['position']['column_min']
                FAB_bottom_edge = embeddedcompos[j]['position']['column_max']
                break
            if (embeddedcompos[j]['name'] == "Keyboard"):
                keyboard = True
                break
            if (embeddedcompos[j]['name'] == "snackbar"):
                snackbar = True
                snackbar_bottom_edge = embeddedcompos[j]['position']['column_max']
                break
        # Call Functions
        app_bar_actions(FAB, len(embeddedcompos))
        FAB_placement(bar_top_edge, FAB_top_edge, FAB_bottom_edge)
        cover_bottom_bar(keyboard)
        snackbar_toast(snackbar, snackbar_bottom_edge,
                       bar_top_edge, FAB_top_edge)

    return


# Guideline 1

def app_bar_actions(FAB, actions):
    if (FAB):
        if (actions <= 2):
            return "Error"
    elif (actions <= 1):
        return "Error"
    return "Success"


# Guideline 7

def FAB_placement(bar_top_edge, FAB_top_edge, FAB_bottom_edge):
    if (FAB_bottom_edge + FAB_top_edge)/2 == bar_top_edge:
        return "Success"
    return "Error"


# Guideline 8

def cover_bottom_bar(keyboard):
    if (keyboard):
        return "Error"
    return "Success"


# Guideline 3

def snackbar_toast(snackbar, snackbar_bottom_edge, bar_top_edge, FAB_top_edge):
    if (snackbar):
        if (snackbar_bottom_edge > FAB_top_edge):
            return "Success"
    if (snackbar_bottom_edge > bar_top_edge):
        return "Success"
    return "Error"

#############################
### Icon detection needed ###
#############################


# def nav_outside_bottom_bar(nav_bottom_edge, bar_top_edge):
#     if (nav_bottom_edge > bar_top_edge):
#         return "Success"
#     return "Error"


# def app_bar_nav_menu(nav_menu, count):
#     if (nav_menu == True, count > 1):
#         return "Success"
#     return "Error"


# def overflow_menu(top_bar, top_bottom_edge, bottom_bar, overflow, overflow_loc):
#     if (top_bar == True and bottom_bar == True):
#         if (overflow == True and (overflow_loc > top_bottom_edge)):
#             return "Success"
#     return "Error"

# def FAB_anatomy(nav, actions, type):
#     if type == "centered":
#         if (nav == True and actions >= 1):
#             return "Success"
#         return "Error"
#     elif type == "end":
#         if actions >= 3 and actions <= 4:
#             return "Success"
#         return "Error"
#     elif type == "landscape":
#         return "Error"
#     else:
#         if (nav == True and actions <= 4):
#             return "Success"
#         return "Error"
