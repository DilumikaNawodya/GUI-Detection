def cards_main(data, i, ncomponents):
    Ids = []
    card = data['combinedjson']['compos'][i]
    embeddedtext = card.get('embeddedtext')

    # Call Functions
    if (embeddedtext):
        Ids.append(card_content(embeddedtext))
    return Ids


def card_content(embeddedtext):
    text_height = embeddedtext[0]['height']
    if (text_height > 6):
        return 85
    return -1
