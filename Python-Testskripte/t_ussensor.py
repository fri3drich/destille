#Quelle: https://tutorials-raspberrypi.de/entfernung-messen-mit-ultraschallsensor-hc-sr04/
#Datum: 01.10.2018
#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
 
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def Fuellstand():
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
 
    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
 
    # Zeit Differenz zwischen Start und Ankunft
    DifferenzZeit = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    Distanz = (DifferenzZeit * 34300) / 2

    #Berechnung Anzeige Kuehlwasser Fuellstand 0-100%
    #m= (y2-y1)/(x2-x1)
    #b= y2-(m*x2)
    #y= m x + b
    b = 123.3     #Muss berechnet werden: y=mx+b // m= (y2-y1)/(x2-x1)
    x1 = 2.5    #x1 = Hoehe vom Sensor bis Soll-Maximale-Fuellstandshoehe in cm
    x2 = 13.5   #x2 = Entfernung Ultraschall-Sensor bis Boden in cm
    y1 = 100    #in % //Leer =   0%
    y2 = 0      #in % //Voll= 100%
    
    #Berechnung Wert der Steigung
    Steigung = (y2-y1)/(x2-x1)
    
    #Berechnung des Fuellstandes in %
    Fuellstand = Steigung * Distanz + b
 
    return(Fuellstand)

 

try:
    while True:
        abstand = Fuellstand()
        print ("Gemessene Entfernung = %.1f in Prozent" % abstand)
        time.sleep(1)
 
    # Beim Abbruch durch STRG+C resetten
except KeyboardInterrupt:
    print("Messung vom User gestoppt")
    GPIO.cleanup()
