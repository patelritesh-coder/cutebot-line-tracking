basic.show_leds("""
    . . . # .
        # . # . #
        # . # . #
        # . # . #
        . # . . .
""")

def on_forever():
    if cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(50, 25)
    if cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(25, 50)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        cuteBot.motors(50, 50)
basic.forever(on_forever)