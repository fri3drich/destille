#Quelle: https://tutorials-raspberrypi.de/raspberry-pi-temperatur-mittels-sensor-messen/
#Datum: 01.10.2018
#sys und time Libary importieren
import sys
import time

try:
    def DampfTemperatur():
        #1-wire-Bus Datei auslesen von Temperatur-Sensor 3//Adresse: 28-0316805edfff
        File_Temperatursensor_3 = open('/sys/bus/w1/devices/28-0316805edfff/w1_slave')
        Filecontent_Temperatursensor_3 = File_Temperatursensor_3.read()
        File_Temperatursensor_3.close()

        #Temperaturwert extrahieren und von mC in C umrechnen
        String_Temperatursensor_3 = Filecontent_Temperatursensor_3.split("\n")[1].split(" ")[9]
        Wert_Temperatursensor_3 = float(String_Temperatursensor_3[2:]) / 1000

        #Temperatur ausgeben
        DampfTemperatur = '%6.2f' % Wert_Temperatursensor_3
        return (DampfTemperatur)
  
    i = 1

    while i == 1:
        messdaten = DampfTemperatur()
	print "Aktuelle Wassertemperatur : ", messdaten, "C"
	time.sleep(1)

except KeyboardInterrupt:
    print "Temperaturabfrage beendet"
