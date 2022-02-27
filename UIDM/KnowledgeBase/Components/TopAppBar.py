def topappbar_main(data, i, ncomponents):
    # Call Functions
    return


def image_on_app_bar(image, text_detect, text_meta):
    if (image == True):
        if (text_detect == text_meta):
            return "Success"
    return "Error"


def app_bar_text(top_type, text_meta, text_lines, text_detect):
    if (text_meta == text_detect):
        if (text_lines == 2):
            if (top_type == "prominent"):
                return "Success"
    return "Error"
