def lists_main(data, i, ncomponents, screen_size):
    List = data['combinedjson']['compos'][i]
    embeddedcompos = List.get('embeddedcompos')

    # Call Functions
    if (embeddedcompos):
        thumbnail_loc(embeddedcompos)
        divider_per_item(embeddedcompos)
    return


def thumbnail_loc(embeddedcompos, screen_size):
    thumbnail = -1
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "thumbnail":
            thumbnail = i
            break
    if thumbnail != -1:
        thumbnail_left_edge = embeddedcompos[thumbnail]['column_min']
    screen_width = screen_size[0]
    if (thumbnail_left_edge < screen_width/4):
        return "Success"
    if (thumbnail_left_edge > screen_width/4 and thumbnail_left_edge < 3*screen_width/4):
        return "Caution"


def divider_per_item(embeddedcompos, item_space):
    divider = False
    for i in len(embeddedcompos):
        if embeddedcompos[i]['name'] == "Divider":
            divider = True
    if (len(embeddedcompos)//2 > 1):
        if (divider):
            return "Success"
        if ((embeddedcompos[1]['position']['row_max']-embeddedcompos[1]['position']['row_max']) > 5):
            return "Caution"
        return "Error"
    return "Success"
