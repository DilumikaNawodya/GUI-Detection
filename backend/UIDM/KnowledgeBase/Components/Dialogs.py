def dialogs_main(data, i, ncomponents):
    Ids = []
    dialog = data['combinedjson']['compos'][i]
    embeddedcompos = dialog.get('embeddedcompos')
    embeddedtext = dialog.get('embeddedtext')

    # Call Functions
    if (embeddedcompos):
        Ids.append(dialog_actions(embeddedcompos))
    if (embeddedtext):
        Ids.append(dialog_title_content(dialog, embeddedtext))
        Ids.append(dialog_title(embeddedtext))
    return Ids


def dialog_actions(embeddedcompos):
    button_count = 0
    for i in range(len(embeddedcompos)):
        if embeddedcompos[i]['name'] == "Button":
            button_count += 1
    if (button_count == 2):
        return -1
    return 9


def dialog_title(embeddedtext):
    if (embeddedtext[0]['text_content'] == embeddedtext[0]['text_meta']):
        return -1
    return 11


def dialog_title_content(dialog, embeddedtext):
    topbar_bottom_edge = dialog['position']['row_max']
    text_top_edge = embeddedtext[0]['position']['row_min']
    if (topbar_bottom_edge > text_top_edge):
        return -1
    return 12
