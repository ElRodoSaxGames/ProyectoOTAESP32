from machine import Pin
import time

# Cambia a 2 si tu LED está en GPIO2 (lo más común)
LED_PIN = 2

led = Pin(LED_PIN, Pin.OUT)

def run():
    while True:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
