input.onButtonPressed(Button.A, function () {
    Moisture = pins.analogReadPin(AnalogPin.P1)
    if (Moisture <= 400) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(2500)
    basic.clearScreen()
})
let Moisture = 0
led.setBrightness(64)
