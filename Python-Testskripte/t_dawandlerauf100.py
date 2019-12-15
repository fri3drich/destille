#Quelle: http://www.horter.de/blog/i2c-analog-output-4-kanaele-10-bit/
#Datum: 01.10.2018
#Zeit und smbus Libary importieren
import smbus
import time
bus = smbus.SMBus(1)

#Dezimalzahl des Ausgangswertes
Analogausgang_dezi = 100
#Highbyte des Ausgangswertes berechnen
Highbyte = int(Analogausgang_dezi / 256)
#Lowbyte des Ausgangswertes berechnen
Lowbyte = int(Analogausgang_dezi - Highbyte * 256)
#Ausgangswort zusammenstellen aus Low- und Highbyte
Analogausgang_wort = [Lowbyte, Highbyte]
#Ausgangswort ueber i2c-Bus auf den Digital/Analogwandler schreiben
bus.write_i2c_block_data (0x58, 0x00, Analogausgang_wort)
time.sleep(1)
print (Analogausgang_dezi)

