def lists_main(data, i, ncomponents):
    # Call Functions
    return


def thumbnail_loc(thumbnail_left_edge, screen_width):
    if (thumbnail_left_edge < screen_width/4):
        return "Success"
    if (thumbnail_left_edge > screen_width/4 and thumbnail_left_edge < 3*screen_width/4):
        return "Caution"


def divider_per_item(item_lines, dividers, item_space):
    if (item_lines > 1):
        if (dividers):
            return "Success"
        if (item_space > 5):
            return "Caution"
        return "Error"
    return "Success"

# Adjust margins to create a more comfortable line length for reading.

# Don’t scale components without adjusting other affected areas of the screen, such as text length. This can result in line lengths that make reading difficult.

# A multi-column layout can help break up content when needed.
