def button_main(data, i, ncomponents):
    button = data['combinedjson']['compos'][i]
    embeddedtext = button.get('embeddedtext')

    # Call Functions
    if (embeddedtext):
        button_text_wrap(len(embeddedtext))
    return


def button_text_wrap(text_lines):
    if (text_lines > 1):
        return "Error"
    return "Success"
