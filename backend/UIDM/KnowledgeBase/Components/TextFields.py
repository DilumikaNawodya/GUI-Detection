def textfield_main(data, i, ncomponents):
    Ids = []
    TextField = data['combinedjson']['compos'][i]
    embeddedcompos = TextField.get('embeddedcompos')
    embeddedtext = TextField.get('embeddedtext')
    textmeta = TextField.get('textmeta')

    # Call Functions
    Ids.append(Text_Field_Labels(embeddedtext))
    if (embeddedtext):
        Ids.append(Text_Field_Label_MultiLine(embeddedtext))
        if (textmeta):
            Ids.append(Text_Field_Label_Truncate(embeddedtext,textmeta))
    return


def Text_Field_Labels(embeddedtext):
    if (embeddedtext):
        return -1
    return 28

def Text_Field_Label_Truncate(embeddedtext,textmeta):
    if (embeddedtext[0]['text_content']==textmeta['text_content']):
        return -1
    return 29

def Text_Field_Label_MultiLine(embeddedtext):
    if len(embeddedtext)>1:
        return 30
    return -1