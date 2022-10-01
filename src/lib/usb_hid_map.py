keyboard_special_key_map = {
    'enter':        0x28,
    'esc':          0x29,
    'backspace':    0x2a,
    'tab':          0x2b,
    'space':        0x2c,
    'prtscr':       0x46,
    'pause':        0x48,
    'insert':       0x49,
    'home':         0x4a,
    'pageup':       0x4b,
    'del':          0x4c,
    'end':          0x4d,
    'pagedown':     0x4e,
    'rightarrow':   0x4f,
    'leftarrow':    0x50,
    'downarrow':    0x51,
    'uparrow':      0x52,
    'lcontrol':     0xe0,
    'lshift':       0xe1,
    'lalt':         0xe2,
    'lgui':         0xe3, #Windows Key
    'rcontrol':     0xe4,
    'rshift':       0xe5,
    'ralt':         0xe6,
    'rgui':         0xe7 
}

keyboard_fkeys_map = {
    'F1':   0x3a,
    'F2':   0x3b,
    'F3':   0x3c,
    'F4':   0x3d,
    'F5':   0x3e,
    'F6':   0x3f,
    'F7':   0x40,
    'F8':   0x41,
    'F9':   0x42,
    'F10':  0x43,
    'F11':  0x44,
    'F12':  0x45,
    'F13':  0x68,
    'F14':  0x69,
    'F15':  0x6a,
    'F16':  0x6b,
    'F17':  0x6c,
    'F18':  0x6d,
    'F19':  0x6e,
    'F20':  0x6f,
    'F21':  0x70,
    'F22':  0x71,
    'F23':  0x72,
    'F24':  0x73
}


fkeys = keyboard_fkeys_map
special = keyboard_special_key_map

F1 = fkeys['F1']
F2 = fkeys['F2']
F3 = fkeys['F3']
F4 = fkeys['F4']
F5 = fkeys['F5']
F6 = fkeys['F6']
F7 = fkeys['F7']
F8 = fkeys['F8']
F9 = fkeys['F9']
F10 = fkeys['F10']
F11 = fkeys['F11']
F12 = fkeys['F12']
F13 = fkeys['F13']
F14 = fkeys['F14']
F15 = fkeys['F15']
F16 = fkeys['F16']
F17 = fkeys['F17']
F18 = fkeys['F18']
F19 = fkeys['F19']
F20 = fkeys['F20']
F21 = fkeys['F21']
F22 = fkeys['F22']
F23 = fkeys['F23']
F24 = fkeys['F24']

ENTER = special['enter']
ESC = special['esc']
BACKSPACE = special['backspace']
TAB = special['tab']
SPACE = special['space']
PRTSCR = special['prtscr']
PAUSE = special['pause']
INSERT = special['insert']
HOME = special['home']
PAGEUP = special['pageup']
PAGEDOWN = special['pagedown']
DEL = special['del']
END = special['end']
RIGHT_ARROW = special['rightarrow']
LEFT_ARROW = special['leftarrow']
UP_ARROW = special['uparrow']
DOWN_ARROW = special['downarrow']
LEFT_SHIFT = special['lshift']
LEFT_CONTROL = special['lcontrol']
LEFT_ALT = special['lalt']
LEFT_GUI = special['lgui']
RIGHT_SHIFT = special['rshift']
RIGHT_CONTROL = special['rcontrol']
RIGHT_ALT = special['ralt']
RIGHT_GUI = special['rgui']
WIN = LEFT_GUI
SHIFT = LEFT_SHIFT
ALT = LEFT_ALT
CTRL = LEFT_CONTROL
COMMAND = LEFT_GUI
OPTION = LEFT_ALT

keyboard_character_map = {
    ' ': SPACE,
    'a': 0x04,
    'b': 0x05,
    'c': 0x06,
    'd': 0x07,
    'e': 0x08,
    'f': 0x09,
    'g': 0x0a,
    'h': 0x0b,
    'i': 0x0c,
    'j': 0x0d,
    'k': 0x0e,
    'l': 0x0f,
    'm': 0x10,
    'n': 0x11,
    'o': 0x12,
    'p': 0x13,
    'q': 0x14,
    'r': 0x15,
    's': 0x16,
    't': 0x17,
    'u': 0x18,
    'v': 0x19,
    'w': 0x1a,
    'x': 0x1b,
    'y': 0x1c,
    'z': 0x1d,
    'A': [SHIFT, 0x04],
    'B': [SHIFT, 0x05],
    'C': [SHIFT, 0x06],
    'D': [SHIFT, 0x07],
    'E': [SHIFT, 0x08],
    'F': [SHIFT, 0x09],
    'G': [SHIFT, 0x0a],
    'H': [SHIFT, 0x0b],
    'I': [SHIFT, 0x0c],
    'J': [SHIFT, 0x0d],
    'K': [SHIFT, 0x0e],
    'L': [SHIFT, 0x0f],
    'M': [SHIFT, 0x10],
    'N': [SHIFT, 0x11],
    'O': [SHIFT, 0x12],
    'P': [SHIFT, 0x13],
    'Q': [SHIFT, 0x14],
    'R': [SHIFT, 0x15],
    'S': [SHIFT, 0x16],
    'T': [SHIFT, 0x17],
    'U': [SHIFT, 0x18],
    'V': [SHIFT, 0x19],
    'W': [SHIFT, 0x1a],
    'X': [SHIFT, 0x1b],
    'Y': [SHIFT, 0x1c],
    'Z': [SHIFT, 0x1d],
    '1': 0x1e, 
    '2': 0x1f,
    '3': 0x20,
    '4': 0x21,
    '5': 0x22,
    '6': 0x23,
    '7': 0x24,
    '8': 0x25,
    '9': 0x26,
    '0': 0x27,
    '-': 0x2D,
    '=': 0x2E,
    '[': 0x2F,
    ']': 0x30,
    ';': 0x33,
    '`': 0x35,
    ',': 0x36,
    '.': 0x37,
    '/': 0x38,
    '!': [SHIFT, 0x1e],
    '@': [SHIFT, 0x1f],
    '#': [SHIFT, 0x20],
    '$': [SHIFT, 0x21],
    '%': [SHIFT, 0x22],
    '^': [SHIFT, 0x23],
    '&': [SHIFT, 0x24],
    '*': [SHIFT, 0x25],
    '(': [SHIFT, 0x26],
    ')': [SHIFT, 0x27],
    '_': [SHIFT, 0x2D],
    '+': [SHIFT, 0x2E],
    '{': [SHIFT, 0x2F],
    '}': [SHIFT, 0x30],
    '|': [SHIFT, 0x31],
    ':': [SHIFT, 0x33],
    '"': [SHIFT, 0x34],
    '~': [SHIFT, 0x35],
    '<': [SHIFT, 0x36],
    '>': [SHIFT, 0x37],
    '?': [SHIFT, 0x38]
}

keyboard_character_map['\\'] = 0x31 #|
keyboard_character_map['\''] = 0x34 #"
keys = keyboard_character_map

#SPECIAL COMMANDS
CTRLALTDEL = [CTRL, ALT, DEL]
RUN = [WIN, keys['r']]
SPOTLIGHT = [COMMAND, SPACE]
CLOSE = [ALT, F4]

def get_sequence(user_input):
    sequence = []
    for char in user_input:
        if char in keys.keys():
            sequence.append(keys[char])
    return sequence