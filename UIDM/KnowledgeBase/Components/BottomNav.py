def bottomNav_main(data, i, ncomponents):
    # Call Functions
    return


def n_destinations(icon_count):
    if (icon_count < 3 or icon_count > 5):
        return "Error"
    return "Success"


def tabs_w_bottomnav(tabs, bottomnav):
    if (tabs and bottomnav):
        return "Caution"
    return "Error"


def text_trunacate(text_meta, text_detect):
    for i in len(text_detect):
        text_detect[i] == text_meta[i]
        return "Success"
    return "Error"


def text_size(text_detect_size):
    result = all(height == text_detect_size[0] for height in text_detect_size)
    if (result):
        return "Success"
    return "Error"


def text_lines_banner(text_line):
    if (text_line > 1):
        return "Caution"
    return "Success"

# Use the Primary or High-Emphasis “On” color for the active destination in a bottom navigation bar.


def destination_color(destination_colors):
    color_set = set(destination_colors)
    if (color_set > 2):
        return "Error"
    return "Success"

# On mobile (in landscape mode) or tablet, bottom navigation destinations can retain the same spacing used in portrait mode, rather than being equally distributed across the bottom app bar.

# On mobile (in landscape mode) or tablet, bottom navigation destinations can be positioned horizontally instead of stacked. In this case, it’s recommended that destinations are evenly distributed across the entire bar.
