def dialogs_main(data, i, ncomponents):
    dialog = data['combinedjson']['compos'][i]
    embeddedcompos = dialog.get('embeddedcompos')
    embeddedtext = dialog.get('embeddedtext')
    textmeta = dialog.get('textmeta')

    # Call Functions
    if (embeddedcompos):
        dialog_actions(embeddedcompos)
    if (embeddedtext):
        dialog_title_content(dialog, embeddedtext)
        if (textmeta):
            dialog_title(embeddedtext, textmeta)
    return


def dialog_actions(embeddedcompos):
    button_count = 0
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "Button":
            button_count += 1
    if (button_count == 2):
        return "Success"
    return "Error"


# def dialog_close(close_button):
#     if (close_button):
#         return "Error"
#     return "Success"


def dialog_title(embeddedtext, textmeta):
    if (embeddedtext[0]['text_content'] == textmeta):
        return "Success"
    return "Caution"


def dialog_title_content(dialog, embeddedtext):
    topbar_bottom_edge = dialog['position']['row_max']
    text_top_edge = embeddedtext[0]['position']['row_min']
    if (topbar_bottom_edge > text_top_edge):
        return "Success"
    return "Error"
