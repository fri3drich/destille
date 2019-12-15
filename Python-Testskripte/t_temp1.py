#Quelle: https://tutorials-raspberrypi.de/raspberry-pi-temperatur-mittels-sensor-messen/
#Datum: 01.10.2018
#sys und time Libary importieren
import sys
import time

try:
    def WasserTemperatur():
        #1-wire-Bus Datei auslesen von Temperatur-Sensor 1//Adresse: 28-031680630cff
        File_Temperatursensor_2 = open('/sys/bus/w1/devices/28-03168086a9ff/w1_slave')
        Filecontent_Temperatursensor_2 = File_Temperatursensor_2.read()
        File_Temperatursensor_2.close()

        #Temperaturwert extrahieren und von mC in C umrechnen
        String_Temperatursensor_2 = Filecontent_Temperatursensor_2.split("\n")[1].split(" ")[9]
        WasserTemperatur = float(String_Temperatursensor_2[2:]) / 1000

        #Temperatur ausgeben
        return (WasserTemperatur)
  
    i = 1

    while i == 1:
        messdaten = WasserTemperatur()
	print "Aktuelle Wassertemperatur : ", messdaten, "C"
	time.sleep(1)

except KeyboardInterrupt:
    print "Temperaturabfrage beendet"
