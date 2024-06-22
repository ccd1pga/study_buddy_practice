# my_toolbox/my_toolbox.py

# Coloured text: colored_text("text", "color")
from IPython.display import display, Markdown

# ANSI escape codes for coloring text
def colored_text(text, color):
    colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        'bright_red': '91',
        'bright_green': '92',
        'bright_yellow': '93',
        'bright_blue': '94',
        'bright_magenta': '95',
        'bright_cyan': '96',
        'bright_white': '97'
    }
    return f"{colors[color]}{text}{colors['reset']}"


# Add more functions as needed
