#Zeit und GPIO Libary importieren
import RPi.GPIO as GPIO
import time

#GPIO Boardnummern
GPIO.setmode(GPIO.BCM)

#GPIOs zureucksetzen
GPIO.cleanup()

#GPIO Variablen setzen
RELAIS_1_GPIO = 26
RELAIS_2_GPIO = 19
RELAIS_3_GPIO = 13
RELAIS_4_GPIO = 6

#GPIO als Ausgang deklarieren
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT)

#Relais  an
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
time.sleep(1)
GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
time.sleep(1)
GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
time.sleep(1)
GPIO.output(RELAIS_4_GPIO, GPIO.LOW)

time.sleep(5)

#Relais aus
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
time.sleep(3)
GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
time.sleep(3)
GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
time.sleep(3)
GPIO.output(RELAIS_4_GPIO, GPIO.HIGH)
GPIO.cleanup()
