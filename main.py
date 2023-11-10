def on_button_pressed_a():
    global Moisture
    Moisture = pins.analog_read_pin(AnalogPin.P1)
    if Moisture <= 400:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)
    basic.pause(2500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

Moisture = 0
led.set_brightness(64)