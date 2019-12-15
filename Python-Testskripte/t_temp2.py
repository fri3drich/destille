#Quelle: https://tutorials-raspberrypi.de/raspberry-pi-temperatur-mittels-sensor-messen/
#Datum: 01.10.2018
#sys und time Libary importieren
import sys
import time

try:
    def InhaltTemperatur():
        #1-wire-Bus Datei auslesen von Temperatur-Sensor 2//Adresse: 28-03168086a9ff
        File_Temperatursensor_1 = open('/sys/bus/w1/devices/28-031680630cff/w1_slave')
        Filecontent_Temperatursensor_1 = File_Temperatursensor_1.read()
        File_Temperatursensor_1.close()

        #Temperaturwert extrahieren und von mC in C umrechnen
        String_Temperatursensor_1 = Filecontent_Temperatursensor_1.split("\n")[1].split(" ")[9]
        InhaltTemperatur = float(String_Temperatursensor_1[2:]) / 1000

        #Temperatur ausgeben
        return (InhaltTemperatur)
  
    i = 1

    while i == 1:
        messdaten = InhaltTemperatur()
	print "Aktuelle Inhalttemperatur : ", messdaten, "C"
	time.sleep(1)

except KeyboardInterrupt:
    print "Temperaturabfrage beendet"
