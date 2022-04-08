def topappbar_main(data, i, ncomponents):
    Ids = []
    TopAppBar = data['combinedjson']['compos'][i]
    embeddedcompos = TopAppBar.get('embeddedcompos')
    embeddedtext = TopAppBar.get('embeddedtext')
    text_meta = TopAppBar.get('textmeta')

    # Call Functions
    if (embeddedcompos and embeddedtext and text_meta):
        Ids.append(image_on_app_bar(embeddedcompos, embeddedtext, text_meta))
    return Ids


def image_on_app_bar(embeddedcompos, embeddedtext, text_meta):
    image = False
    if (embeddedcompos[0]['name'] == "Image"):
        image = True
    if (image == True):
        if (embeddedtext[0]['text_content'] == text_meta):
            return "Success"
    return "Error"

########################################
### Type detection needs to be added ###
########################################

# def app_bar_text(top_type, text_meta, text_lines, text_detect):
#     if (text_meta == text_detect):
#         if (text_lines == 2):
#             if (top_type == "prominent"):
#                 return "Success"
#     return "Error"
