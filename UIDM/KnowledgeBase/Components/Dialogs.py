def dialogs_main(data, i, ncomponents):
    # Call Functions
    return


def dialog_actions(button_count):
    if (button_count == 2):
        return "Success"
    return "Error"


def dialog_close(close_button):
    if (close_button):
        return "Error"
    return "Success"


def dialog_title(text_detect, text_meta):
    if (text_detect == text_meta):
        return "Success"
    return "Caution"


def dialog_title_content(topbar_bottom_edge, text_top_edge):
    if (topbar_bottom_edge > text_top_edge):
        return "Success"
    return "Error"
