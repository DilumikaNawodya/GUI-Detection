def button_main(data, i, ncomponents):
    button = data['combinedjson']['compos'][i]
    embeddedcompos = button['embeddedcompos']
    embeddedtext = button['embeddedtext']

    # Call Functions
    button_text_wrap(len(embeddedtext))
    return

# Use capitalization for languages that allow capitalization.


def button_text_wrap(text_lines):
    if (text_lines > 1):
        return "Error"
    return "Success"

# Avoid using two contained buttons next to one another if they don’t have the same fill color.

# In a bottom bar, when using multiple buttons, you can place a outlined button (medium emphasis) next to a contained button (high emphasis).

# When using multiple buttons in a bottom bar, you can place a text button (low emphasis) next to an outlined button (medium emphasis).
