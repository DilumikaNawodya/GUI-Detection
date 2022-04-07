def tabs_main(data, i, ncomponents):
    Tab = data['combinedjson']['compos'][i]
    embeddedcompos = Tab.get('embeddedcompos')
    embeddedtext = Tab.get('embeddedtext')
    textmeta = Tab.get('textmeta')

    # Call Functions
    if (embeddedtext):
        tab_rows(embeddedtext)
        tabs_text_shrink(embeddedtext)
        if (embeddedcompos):
            tab_label(embeddedcompos, embeddedtext)
        if (textmeta):
            tabs_truncate(embeddedtext, textmeta)
    return


def tab_label(embeddedcompos, embeddedtext):
    if len(embeddedcompos) == len(embeddedtext):
        return "Success"
    return "Error"


def tab_rows(embeddedtext):
    height = embeddedtext[0]['height']
    height_consistency = True
    for i in range(1, len(embeddedtext)):
        if embeddedtext[i]['height'] != height:
            height_consistency = False
    if (height_consistency == False):
        return "Caution"
    return "Success"


def tabs_text_shrink(embeddedtext):
    size = embeddedtext[0]['height']
    size_consistency = True
    for i in range(1, len(embeddedtext)):
        if embeddedtext[i]['height'] != size:
            size_consistency = False
    if (size_consistency == False):
        return "Caution"
    return "Success"


def tabs_truncate(embeddedtext, text_meta):
    text_consistency = True
    for i in len(embeddedtext):
        if embeddedtext[i]['text_content'] != text_meta[i]:
            text_consistency = False
    if (text_consistency == True):
        return "Success"
    return "Error"
