def kelvinToCelcius(suhu):
    ''' Konversi dari Kelvin ke Celcius '''
    konversi = suhu - 273.15
    if (suhu % 1 != 0):
        print(f'\nKonversi suhu dari {suhu} derajat Kelvin adalah {konversi} derajat Celcius')
        return konversi
        
    else:
        suhuInteger = int(suhu)
        print(f'\nKonversi suhu dari {suhuInteger} derajat Kelvin adalah {konversi} derajat Celcius') 
        return konversi
           

def celciusToKelvin(suhu):
    ''' Konversi dari Celcius ke Kelvin '''
    konversi = suhu + 273.15
    if (suhu % 1 != 0):
        print(f'\nKonversi suhu dari {suhu} derajat Celcius adalah {konversi} derajat Kelvin')
        return konversi
    else:
        suhuInteger = int(suhu)
        print(f'\nKonversi suhu dari {suhuInteger} derajat Celcius adalah {konversi} derajat Kelvin')
        return konversi

def celciusToFahrenheit(suhu):
    ''' Konversi dari Celcius ke Fahrenheit '''
    konversi = (suhu*9/5) + 32
    if (suhu % 1 != 0):
        print(f'\nKonversi suhu dari {suhu} derajat Celcius adalah {konversi} derajat Fahrenheit')
        return konversi
    else:
        suhuInteger = int(suhu)
        print(f'\nKonversi suhu dari {suhuInteger} derajat Celcius adalah {konversi} derajat Fahrenheit')
        return konversi

def kelvinToFahrenheit(suhu):
    ''' Konversi dari Kelvin ke Fahrenheit '''
    konversi = (suhu-273.15) * 9 / 5 + 32
    konversiFormat = "{:.2f}".format(konversi)
    if (suhu % 1 != 0):
        print(f'\nKonversi suhu dari {suhu} derajat Kelvin adalah {konversiFormat} derajat Fahrenheit')
        return konversi
    else:
        suhuInteger = int(suhu)
        print(f'\nKonversi suhu dari {suhuInteger} derajat Kelvin adalah {konversiFormat} derajat Fahrenheit')
        return konversi

def fahrenheitToCelcius(suhu):
    ''' Konversi dari Fahrenheit ke Celcius '''
    konversi = (suhu-32) * 5 / 9
    konversiFormat = "{:.2f}".format(konversi)
    if (suhu % 1 != 0):
        print(f'\nKonversi suhu dari {suhu} derajat Fahrenheit adalah {konversiFormat} derajat Celcius')
        return konversi
    else:
        suhuInteger = int(suhu)
        print(f'\nKonversi suhu dari {suhuInteger} derajat Fahrenheit adalah {konversiFormat} derajat Celcius') 
        return konversi

def fahrenheitToKelvin(suhu):
    ''' Konversi dari Fahrenheit ke Kelvin '''
    konversi = (suhu-32) * 5 / 9 + 273.15
    konversiFormat = "{:.2f}".format(konversi)
    if (suhu % 1 != 0):
        print(f'\nKonversi suhu dari {suhu} derajat Fahrenheit adalah {konversiFormat} derajat Kelvin')
        return konversi
    else:
        suhuInteger = int(suhu)
        print(f'\nKonversi suhu dari {suhuInteger} derajat Fahrenheit adalah {konversiFormat} derajat Kelvin')         
        return konversi

inputanSuhu = float(input('\nMasukkan suhu dalam satuan Kelvin: '))
kelvinToCelcius(inputanSuhu)
inputanSuhu = float(input('\nMasukkan suhu dalam satuan Celcius: '))
celciusToKelvin(inputanSuhu)
inputanSuhu = float(input('\nMasukkan suhu dalam satuan Celcius: '))
celciusToFahrenheit(inputanSuhu)
inputanSuhu = float(input('\nMasukkan suhu dalam satuan Kelvin: '))
kelvinToFahrenheit(inputanSuhu)
inputanSuhu = float(input('\nMasukkan suhu dalam satuan Fahrenheit: '))
fahrenheitToCelcius(inputanSuhu)
inputanSuhu = float(input('\nMasukkan suhu dalam satuan Fahrenheit: '))
fahrenheitToKelvin(inputanSuhu)