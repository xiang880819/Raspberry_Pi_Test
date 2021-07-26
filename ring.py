import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(50)


def destory():
    p.stop()
    GPIO.cleanup()


def doReMi():
    while True:
        print("Do")
        p.ChangeFrequency(523)
        time.sleep(1)

        print("Re")
        p.ChangeFrequency(587)
        time.sleep(1)

        print("Mi")
        p.ChangeFrequency(659)
        time.sleep(1)


if __name__ == "__main__":
    try:
        doReMi()
    except KeyboardInterrupt:
        destory()
