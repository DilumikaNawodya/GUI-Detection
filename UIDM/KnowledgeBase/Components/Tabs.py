def tabs_main():
    # Call Functions
    return


def tab_label(text, icon):
    return


def tab_rows(text_lines):
    if (text_lines == 1):
        return "Success"
    return "Caution"


def tabs_text_shrink(text_size):
    if (text_size[0] == text_size[1]):
        return "Success"
    return "Error"


def tabs_truncate(text_detect, text_meta):
    if (text_detect == text_meta):
        return "Success"
    return "Error"
