#Zeit und GPIO Libary importieren
import RPi.GPIO as GPIO
import time

#GPIO Boardnummern
GPIO.setmode(GPIO.BCM)

#GPIOs als Eingang deklarieren
GPIO.setup(12, GPIO.IN)  #Schwimmerschlater
GPIO.setup(16, GPIO.IN)  #SR Q1
GPIO.setup(20, GPIO.IN)  #SR Q2
GPIO.setup(21, GPIO.IN)  #SR Q3
GPIO.setup(25 ,GPIO.IN)	#Automatenfall
GPIO.setup(5 ,GPIO.IN) #Not-aus

try:
        while True:
                if GPIO.input(12) == GPIO.HIGH:
                        print "Schwimmerschalter unten  HIGH"
                if GPIO.input(12) == GPIO.LOW:
                        print "Schwimmerschalter oben LOW"

                if GPIO.input(16) == GPIO.HIGH:
                        print "Q01 aus HIGH"
                if GPIO.input(16) == GPIO.LOW:
                        print "Q01 an LOW"

                if GPIO.input(20) == GPIO.HIGH:
                        print "Q2 aus HIGH"
                if GPIO.input(20) == GPIO.LOW:
                        print "Q2 an LOW"

                if GPIO.input(21) == GPIO.HIGH:
                        print "Q3 aus HIGH"
                if GPIO.input(21) == GPIO.LOW:
                        print "Q3 an LOW"

                if GPIO.input(25) == GPIO.HIGH:
                        print "AUTOMATENFALL FEHLER  HIGH"
                if GPIO.input(25) == GPIO.LOW:
                        print "AUTOMATEN ok  LOW"

                if GPIO.input(5) == GPIO.HIGH:
                        print "NOT AUS AUSgeloest HIGH"
                if GPIO.input(5) == GPIO.LOW:
                        print "NOT AUS ok LOW"

                time.sleep(1)
#Beim Abbruch durch STRG+C resetten
except KeyboardInterrupt:
        print("Durch STRG+C gestoppt")
        GPIO.cleanup()
