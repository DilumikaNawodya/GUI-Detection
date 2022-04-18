def topappbar_main(data, i, ncomponents):
    Ids = []
    TopAppBar = data['combinedjson']['compos'][i]
    embeddedcompos = TopAppBar.get('embeddedcompos')
    embeddedtext = TopAppBar.get('embeddedtext')

    # Call Functions
    if (embeddedcompos and embeddedtext):
        Ids.append(image_on_app_bar(embeddedcompos, embeddedtext))
    return Ids


def image_on_app_bar(embeddedcompos, embeddedtext):
    image = False
    if (embeddedcompos[0]['name'] == "Image"):
        image = True
    if (image == True):
        if (embeddedtext[0]['text_content'] == embeddedtext[0]['text_meta']):
            return -1
    return 102
