'''
�rskostnader elbil vs bensinbil

Av Ingvild B. Hvidsten ingvildh@gmail.com

Oppdatert 29.10.2024
'''

#%% Definerte konstanter

Trafikkforsikringsavgift = 8.38  # [kr/dag]
Forsikring_Elbil = 5000  # [kr/�r]
Forsikring_Bensinbil = 7500  # [kr/�r]
Dager_i_�ret = 365  # [antall dager/�r]
Drivstoff_elbil = 0.2  # kWh/km
Str�mpris = 2.00  # [kr/kWh]
Drivstoff_Bensinbil = 1.0  # [kr/km]
Bomavgift_Elbil = 0.1  # [kr/km]
Bomavgift_Bensinbil = 0.3  # [kr/km]

#%% Definisjon av antall kilomenter per �ret

Km_i_�ret = float(input('Oppgi forventet antall kilometer per �r: '))

#%% Beregning av �rskostnad elbil

Trafikkforsikringsavgift_elbil = Trafikkforsikringsavgift * Dager_i_�ret
Drivstoffkostnad_elbil = Drivstoff_elbil * Str�mpris * Km_i_�ret
Bomavgift_�r_elbil = Bomavgift_Elbil * Km_i_�ret
Total_elbil_�r = Trafikkforsikringsavgift_elbil + Drivstoffkostnad_elbil + Bomavgift_�r_elbil + Forsikring_Elbil


#%% Beregning av �rskostnad bensinbil

Trafikkforsikringsavgift_bensinbil = Trafikkforsikringsavgift * Dager_i_�ret
Drivstoffkostnad_bensinbil = Drivstoff_Bensinbil * Km_i_�ret
Bomavgift_�r_bensinbil = Bomavgift_Bensinbil * Km_i_�ret
Total_bensinbil_�r = Trafikkforsikringsavgift_bensinbil + Drivstoffkostnad_bensinbil + Bomavgift_�r_elbil + Forsikring_Bensinbil


#%% Utskrift

if Km_i_�ret > 1:
    print('�rskostnaden for elbil er kr.', Total_elbil_�r, 'mens �rskostnaden for bensinbil er kr', Total_bensinbil_�r)
elif Km_i_�ret == 0: 
    print('�rskostnaden for elbil er kr.', Total_elbil_�r, 'mens �rskostnaden for bensinbil er kr', Total_bensinbil_�r)
else: print('Vennligst oppgi et gyldig antall kilometer.')


