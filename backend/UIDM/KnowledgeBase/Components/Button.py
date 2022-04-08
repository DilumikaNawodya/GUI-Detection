def button_main(data, i, ncomponents):
    Ids = []
    button = data['combinedjson']['compos'][i]
    embeddedtext = button.get('embeddedtext')
    print("Button_main")

    # Call Functions
    if (embeddedtext):
        Ids.append(button_text_wrap(len(embeddedtext)))
        print(Ids)
    return Ids


def button_text_wrap(text_lines):
    print("button_text_wrap")
    if (text_lines > 1):
        return 59
    return -1
