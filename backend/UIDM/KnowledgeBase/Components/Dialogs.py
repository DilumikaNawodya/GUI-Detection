def dialogs_main(data, i, ncomponents):
    Ids = []
    dialog = data['combinedjson']['compos'][i]
    embeddedcompos = dialog.get('embeddedcompos')
    embeddedtext = dialog.get('embeddedtext')
    textmeta = dialog.get('textmeta')

    # Call Functions
    if (embeddedcompos):
        Ids.append(dialog_actions(embeddedcompos))
    if (embeddedtext):
        Ids.append(dialog_title_content(dialog, embeddedtext))
        if (textmeta):
            Ids.append(dialog_title(embeddedtext, textmeta))
    return Ids


def dialog_actions(embeddedcompos):
    button_count = 0
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "Button":
            button_count += 1
    if (button_count == 2):
        return -1
    return 9


def dialog_title(embeddedtext, textmeta):
    if (embeddedtext[0]['text_content'] == textmeta):
        return -1
    return 11


def dialog_title_content(dialog, embeddedtext):
    topbar_bottom_edge = dialog['position']['row_max']
    text_top_edge = embeddedtext[0]['position']['row_min']
    if (topbar_bottom_edge > text_top_edge):
        return -1
    return 12
