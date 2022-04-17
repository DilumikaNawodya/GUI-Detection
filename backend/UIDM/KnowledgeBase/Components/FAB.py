def fab_main(data, i, ncomponents):
    Ids = []
    FAB = data['combinedjson']['compos'][i]
    embeddedcompos = FAB.get('embeddedcompos')
    embeddedtext = FAB.get('embeddedtext')
    textmeta = FAB.get('textmeta')

    btn_count = 0
    bottom_appbar = False
    for j in range(ncomponents):
        if (data['combinedjson']['compos'][j]['name'] == "Floating Action Button"):
            btn_count += 1
        if (data['combinedjson']['compos'][j]['name'] == "Cards"):
            Card = data['combinedjson']['compos'][j]
        if (data['combinedjson']['compos'][j]['name'] == "Appbar: Bottom"):
            bottom_appbar = True

    # Call Functions
    Ids.append(FAB_count(btn_count))
    Ids.append(Text_Regular_FAB(FAB, embeddedtext))
    Ids.append(FAB_with_Cards(FAB, Card))
    Ids.append(ExFAB_Bottom_Appbar(bottom_appbar, FAB))

    if (embeddedcompos):
        Ids.append(Element_Front_FAB(embeddedcompos))
        if (embeddedtext):
            Ids.append(ExFAB_Only_Icon(embeddedcompos, embeddedtext))
            Ids.append(ExFAB_Text_Wrap(embeddedtext))
            if (textmeta):
                Ids.append(ExFAB_Truncate(embeddedtext, textmeta))

    return


def FAB_count(btn_count):
    if (btn_count > 1):
        return 72
    return -1


def Element_Front_FAB(embeddedcompos):
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "Badge":
            return 73
    return -1


def Text_Regular_FAB(FAB, embeddedtext):
    if FAB['height'] == FAB['width']:
        if (embeddedtext):
            return 74
    return -1


def FAB_with_Cards(FAB, Card):
    cardembeddedcompos = Card.get('embeddedcompos')
    for i in len(cardembeddedcompos):
        if cardembeddedcompos[i]['name'] == "Floating Action Button":
            if cardembeddedcompos[i]['id'] == FAB['id']:
                return 77
    return -1


def ExFAB_Only_Icon(embeddedcompos, embeddedtext):
    if (not embeddedtext):
        if embeddedcompos[0]['name'] == 'Icon':
            return 81
    return -1


def ExFAB_Truncate(embeddedtext, textmeta):
    if (embeddedtext[0]['text_content'] == textmeta['text_content']):
        return -1
    return 82


def ExFAB_Text_Wrap(embeddedtext):
    if len(embeddedtext) > 1:
        return 83
    return -1


def ExFAB_Bottom_Appbar(bottom_appbar, FAB):
    if (bottom_appbar):
        if FAB['height'] < FAB['width']:
            return 84
    return -1
