def cards_main(data, i, ncomponents):
    card = data['combinedjson']['compos'][i]
    embeddedtext = card.get('embeddedtext')

    # Call Functions
    if (embeddedtext):
        card_content(embeddedtext)
    return


def card_content(embeddedtext):
    text_height = embeddedtext[0]['height']
    if (text_height > 6):
        return "Caution"
    return "Success"
