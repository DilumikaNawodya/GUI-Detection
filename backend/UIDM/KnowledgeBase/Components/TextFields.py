def textfield_main(data, i, ncomponents):
    Ids = []
    TextField = data['combinedjson']['compos'][i]
    embeddedcompos = TextField.get('embeddedcompos')
    embeddedtext = TextField.get('embeddedtext')

    # Call Functions

    if (embeddedtext):
        Ids.append(Text_Field_Label_MultiLine(embeddedtext))
        Ids.append(Text_Field_Label_Truncate(embeddedtext))
        Ids.append(Text_Field_Labels(embeddedtext))
    return Ids


def Text_Field_Labels(embeddedtext):
    if (embeddedtext):
        return -1
    return 28


def Text_Field_Label_Truncate(embeddedtext):
    if (embeddedtext[0]['text_content'] == embeddedtext[0]['text_meta']):
        return -1
    return 29


def Text_Field_Label_MultiLine(embeddedtext):
    if len(embeddedtext) > 1:
        return 30
    return -1
