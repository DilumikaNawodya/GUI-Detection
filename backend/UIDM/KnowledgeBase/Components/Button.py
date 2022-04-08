def button_main(data, i, ncomponents):
    Ids = []
    button = data['combinedjson']['compos'][i]
    embeddedtext = button.get('embeddedtext')

    # Call Functions
    if (embeddedtext):
        Ids.append(button_text_wrap(len(embeddedtext)))
    return Ids


def button_text_wrap(text_lines):
    if (text_lines > 1):
        return 59
    return -1
