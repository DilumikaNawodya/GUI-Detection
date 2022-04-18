def tabs_main(data, i, ncomponents):
    Ids = []
    Tab = data['combinedjson']['compos'][i]
    embeddedcompos = Tab.get('embeddedcompos')
    embeddedtext = Tab.get('embeddedtext')

    # Call Functions
    if (embeddedtext):
        Ids.append(tab_rows(embeddedtext))
        Ids.append(tabs_text_shrink(embeddedtext))
        Ids.append(tabs_truncate(embeddedtext))
        if (embeddedcompos):
            Ids.append(tab_label(embeddedcompos, embeddedtext))

    return Ids


def tab_label(embeddedcompos, embeddedtext):
    if len(embeddedcompos) == len(embeddedtext):
        return -1
    return 13


def tab_rows(embeddedtext):
    height = embeddedtext[0]['height']
    height_consistency = True
    for i in range(1, len(embeddedtext)):
        if embeddedtext[i]['height'] != height:
            height_consistency = False
    if (height_consistency == False):
        return 14
    return -1


def tabs_text_shrink(embeddedtext):
    size = embeddedtext[0]['height']
    size_consistency = True
    for i in range(1, len(embeddedtext)):
        if embeddedtext[i]['height'] != size:
            size_consistency = False
    if (size_consistency == False):
        return 16
    return -1


def tabs_truncate(embeddedtext):
    text_consistency = True
    for i in range(len(embeddedtext)):
        if embeddedtext[i]['text_content'] != embeddedtext[i]['text_meta']:
            text_consistency = False
    if (text_consistency == True):
        return -1
    return 17
