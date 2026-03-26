import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5)
keyboard.row_pins = (board.GP7, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.GP8, board.GP9, board.GP11, False),
)
keyboard.modules.append(encoder_handler)

oled_ext = Oled(
    OledData(
        corner_one  ={0: OledReactionType.STATIC, 1: ["KMK"]},
        corner_two  ={0: OledReactionType.LAYER,  1: ["BASE", "FN"]},
        corner_three={0: OledReactionType.STATIC, 1: [""]},
        corner_four ={0: OledReactionType.STATIC, 1: [""]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.modules.append(oled_ext)

keyboard.keymap = [
    [
        KC.MUTE, KC.VOLD, KC.VOLU, KC.MPLY,
        KC.BTN1, KC.BTN2, KC.BTN3, KC.MO(1),
    ],
    [
        KC.TRNS, KC.MPRV, KC.MNXT, KC.MSTP,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.MPRV, KC.MNXT),),
]

if __name__ == "__main__":
    keyboard.go()
