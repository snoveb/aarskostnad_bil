'''
Årskostnader elbil vs bensinbil

Av Ingvild B. Hvidsten ingvildh@gmail.com

Oppdatert 29.10.2024
'''

#%% Definerte konstanter

Trafikkforsikringsavgift = 8.38  # [kr/dag]
Forsikring_Elbil = 5000  # [kr/år]
Forsikring_Bensinbil = 7500  # [kr/år]
Dager_i_året = 365  # [antall dager/år]
Drivstoff_elbil = 0.2  # kWh/km
Strømpris = 2.00  # [kr/kWh]
Drivstoff_Bensinbil = 1.0  # [kr/km]
Bomavgift_Elbil = 0.1  # [kr/km]
Bomavgift_Bensinbil = 0.3  # [kr/km]

#%% Definisjon av antall kilomenter per året

Km_i_året = float(input('Oppgi forventet antall kilometer per år: '))

#%% Beregning av Årskostnad elbil

Trafikkforsikringsavgift_elbil = Trafikkforsikringsavgift * Dager_i_året
Drivstoffkostnad_elbil = Drivstoff_elbil * Strømpris * Km_i_året
Bomavgift_år_elbil = Bomavgift_Elbil * Km_i_året
Total_elbil_år = Trafikkforsikringsavgift_elbil + Drivstoffkostnad_elbil + Bomavgift_år_elbil + Forsikring_Elbil


#%% Beregning av Årskostnad bensinbil

Trafikkforsikringsavgift_bensinbil = Trafikkforsikringsavgift * Dager_i_året
Drivstoffkostnad_bensinbil = Drivstoff_Bensinbil * Km_i_året
Bomavgift_år_bensinbil = Bomavgift_Bensinbil * Km_i_året
Total_bensinbil_år = Trafikkforsikringsavgift_bensinbil + Drivstoffkostnad_bensinbil + Bomavgift_år_elbil + Forsikring_Bensinbil


#%% Utskrift

if Km_i_året > 1:
    print('Årskostnaden for elbil er kr.', Total_elbil_år, 'mens årskostnaden for bensinbil er kr', Total_bensinbil_år)
elif Km_i_året == 0: 
    print('Årskostnaden for elbil er kr.', Total_elbil_år, 'mens årskostnaden for bensinbil er kr', Total_bensinbil_år)
else: print('Vennligst oppgi et gyldig antall kilometer.')


