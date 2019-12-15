#Quelle: https://www.kampis-elektroecke.de/?page_id=3740
#Datum: 01.10.2018
!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Zaehler-Variable, global
Counter = 0
Tic = 0
Hz = float(0)
# Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)
GPIO_DW = 19

# GPIO 18 (Pin 12) als Input definieren und Pullup-Widerstand aktivieren
GPIO.setup(GPIO_DW, GPIO.IN)

# Callback-Funktion
def Interrupt(channel):
  global Counter
  # Counter um eins erhoehen und ausgeben
  Counter = Counter + 1

# Interrupt-Event hinzufuegen, steigende Flanke
GPIO.add_event_detect(GPIO_DW, GPIO.FALLING, callback = Interrupt)

# Endlosschleife, bis Strg-C gedrueckt wird

while Tic < 3:
  Tic = Tic + 1
  print "Tic %d" % Tic
  time.sleep(1)

# Aus Datenblatt
# 120L/h = 16Hz
# 600L/h = 82Hz
# y = mx + b
# 120 = 8 * 16 - 8
Hz = Counter / Tic
Dw = float(8*Hz-8)
DwLmin = float(Dw / 60)
print (Dw)
print  "L/h"
print (DwLmin)
print "L/min"
GPIO.cleanup()
print "\nBye"

