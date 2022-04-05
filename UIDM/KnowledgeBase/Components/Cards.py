def cards_main(data, i, ncomponents):
    card = data['combinedjson']['compos'][i]
    embeddedcompos = card['embeddedcompos']
    embeddedtext = card['embeddedtext']

    # Call Functions
    card_content(embeddedtext)
    return


def card_content(embeddedtext):
    text_height = embeddedtext[0]['height']
    if (text_height > 6):
        return "Caution"
    return "Success"
