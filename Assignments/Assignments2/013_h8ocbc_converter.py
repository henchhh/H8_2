import os
import math
# import string

user = 'dean'
pwd = 'dean123'
opsiMenu = ['No','N','no','n', 'yes','Yes', 'y', 'Y']

def templateMenuUtama():
    print('================== Selamat datang di program untuk Assignment 2 Python Flask ==================\n')
    print("Menu Soal: ")
    print("1. Kelvin ke Celcius dan Celcius ke Kelvin")
    print("2. Kelvin atau Celcius ke Fahrenheit")
    print("3. Fahrenheit ke Kelvin atau Celcius")
    print("4. About")
    print("5. Exit")

def keluarProgram():
    os.system('cls')
    print('\n**************************************')
    print('**************************************')
    print('\nAnda memilih untuk keluar dari program')
    print('\n**************************************')
    print('**************************************')
    print('\n\tProgram akan ditutup\n')
    quit()

def salahUserOrPass():
    os.system('cls')
    print('\n***********************************************')
    print('***********************************************')
    print('\nUsername atau password yang Anda masukan salah!')
    print('\n***********************************************')
    print('***********************************************')
    print('\n\t    Program akan ditutup\n')
    quit()

def about():
    os.system('cls')
    print('================== Ini adalah menu About ==================\n')
    print("Nama lengkap saya : Deandri Firdaus")
    print("Nomor peserta saya : FSDO002ONL013")
    print("Alamat saya : Jakarta Selatan\n")

def menuKelvinCelcius():
    print('================== Selamat datang di program untuk Assignment 2 Python Flask ==================\n')
    print("Menu Soal: ")
    print("1. Kelvin ke Celcius")
    print("2. Celcius ke Kelvin")   

def menuKelvinCelciusToFahrenheit():
    print('================== Selamat datang di program untuk Assignment 2 Python Flask ==================\n')
    print("Menu Soal: ")
    print("1. Kelvin ke Fahrenheit")
    print("2. Celcius ke Fahrenheit") 

def menuFahrenheitToKelvinCelcius():
    print('================== Selamat datang di program untuk Assignment 2 Python Flask ==================\n')
    print("Menu Soal: ")
    print("1. Fahrenheit ke Kelvin")
    print("2. Fahrenheit ke Celcius")     

def tempKelvinCelcius():
    ''' Konversi dari Kelvin ke Celcius dan Celcius ke Kelvin '''
    os.system('cls')
    menuKelvinCelcius()
    inputMenu = input('\nMasukkan pilihan menu yang diinginkan (1 - 2): ')
    while inputMenu not in ['1','2']:
        os.system('cls')
        print("Inputan yang Anda masukkan salah! Mohon untuk input menu yang ditampilkan....\n")
        menuKelvinCelcius()
        inputMenu = (input("\nMohon untuk memasukkan pilihan menu yang diinginkan (1 sampai 2): "))
    if inputMenu == '1':
        os.system('cls')
        print('================== Menu Perhitungan dari Kelvin ke Celcius ==================\n')
        inputanSuhu = float(input('\nMasukkan suhu dalam satuan Kelvin: '))
        kelvinToCelcius(inputanSuhu)
    elif inputMenu == '2':
        os.system('cls')
        print('================== Menu Perhitungan dari Celcius ke Kelvin ==================\n')
        inputanSuhu = float(input('Masukkan suhu dalam satuan Celcius: '))
        celciusToKelvin(inputanSuhu)

def kelvinToCelcius(inputanSuhu: float):
    ''' Konversi dari Kelvin ke Celcius '''
    konversi = inputanSuhu - 273.15
    konversiFormat = math.floor(konversi*100000)/100000
    konversiInteger = math.floor(konversi)
    suhuFormat = math.floor(inputanSuhu*100000)/100000
    suhuInteger = math.floor(inputanSuhu)    
    if ((inputanSuhu % 1 != 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Kelvin adalah {konversiFormat} derajat Celcius')
    elif((inputanSuhu % 1 != 0) and (konversi % 1 == 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Kelvin adalah {konversiInteger} derajat Celcius')
    elif((inputanSuhu % 1 == 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Kelvin adalah {konversiFormat} derajat Celcius')
    else:
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Kelvin adalah {konversiInteger} derajat Celcius')     
    return konversi

def celciusToKelvin(inputanSuhu: float):
    ''' Konversi dari Celcius ke Kelvin '''
    konversi = inputanSuhu + 273.15
    konversiFormat = math.floor(konversi*100000)/100000
    konversiInteger = math.floor(konversi)
    suhuFormat = math.floor(inputanSuhu*100000)/100000
    suhuInteger = math.floor(inputanSuhu)
    if ((inputanSuhu % 1 != 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Celcius adalah {konversiFormat} derajat Kelvin')
    elif((inputanSuhu % 1 != 0) and (konversi % 1 == 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Celcius adalah {konversiInteger} derajat Kelvin')
    elif((inputanSuhu % 1 == 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Celcius adalah {konversiFormat} derajat Kelvin')
    else:
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Celcius adalah {konversiInteger} derajat Kelvin') 
    return konversi

def tempOthersToFahrenheit():
    ''' Konversi dari Kelvin atau Celcius ke Fahrenheit '''
    os.system('cls')
    menuKelvinCelciusToFahrenheit()
    inputMenu = input('\nMasukkan pilihan menu yang diinginkan (1 - 2): ')
    while inputMenu not in ['1','2']:
        os.system('cls')
        print("Inputan yang Anda masukkan salah! Mohon untuk input menu yang ditampilkan....\n")
        menuKelvinCelciusToFahrenheit()
        inputMenu = (input("\nMohon untuk memasukkan pilihan menu yang diinginkan (1 sampai 2): "))
    if inputMenu == '1':
        os.system('cls')
        print('================== Menu Perhitungan dari Kelvin ke Fahrenheit ==================\n')
        inputanSuhu = float(input('\nMasukkan suhu dalam satuan Kelvin: '))
        celciusToFahrenheit(kelvinToCelcius(inputanSuhu))
    elif inputMenu == '2':
        os.system('cls')
        print('================== Menu Perhitungan dari Celcius ke Fahrenheit ==================\n')
        inputanSuhu = float(input('Masukkan suhu dalam satuan Celcius: '))
        kelvinToFahrenheit(celciusToKelvin(inputanSuhu))        

def kelvinToFahrenheit(inputanSuhu: float):
    ''' Konversi dari Kelvin ke Fahrenheit '''
    konversi = (inputanSuhu-273.15) * 9 / 5 + 32
    konversiFormat = math.floor(konversi*100000)/100000
    konversiInteger = math.floor(konversi)
    suhuFormat = math.floor(inputanSuhu*100000)/100000
    suhuInteger = math.floor(inputanSuhu)
    if ((inputanSuhu % 1 != 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Kelvin adalah {konversiFormat} derajat Fahrenheit')
    elif((inputanSuhu % 1 != 0) and (konversi % 1 == 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Kelvin adalah {konversiInteger} derajat Fahrenheit')
    elif((inputanSuhu % 1 == 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Kelvin adalah {konversiFormat} derajat Fahrenheit')
    else:
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Kelvin adalah {konversiInteger} derajat Fahrenheit') 
    return konversi

def celciusToFahrenheit(inputanSuhu: float):
    ''' Konversi dari Celcius ke Fahrenheit '''
    konversi = (inputanSuhu*9/5) + 32
    konversiFormat = math.floor(konversi*100000)/100000
    konversiInteger = math.floor(konversi)
    suhuFormat = math.floor(inputanSuhu*100000)/100000
    suhuInteger = math.floor(inputanSuhu)
    if ((inputanSuhu % 1 != 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Celcius adalah {konversiFormat} derajat Fahrenheit')
    elif((inputanSuhu % 1 != 0) and (konversi % 1 == 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Celcius adalah {konversiInteger} derajat Fahrenheit')
    elif((inputanSuhu % 1 == 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Celcius adalah {konversiFormat} derajat Fahrenheit')
    else:
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Celcius adalah {konversiInteger} derajat Fahrenheit') 
    return konversi

def tempFahrenheitToOthers():
    ''' Konversi dari Fahrenheit ke Kelvin atau Celcius '''
    os.system('cls')
    menuFahrenheitToKelvinCelcius()
    inputMenu = input('\nMasukkan pilihan menu yang diinginkan (1 - 2): ')
    while inputMenu not in ['1','2']:
        os.system('cls')
        print("Inputan yang Anda masukkan salah! Mohon untuk input menu yang ditampilkan....\n")
        menuFahrenheitToKelvinCelcius()
        inputMenu = (input("\nMohon untuk memasukkan pilihan menu yang diinginkan (1 sampai 2): "))
    if inputMenu == '1':
        os.system('cls')
        print('================== Menu Perhitungan dari Fahrenheit ke Kelvin ==================\n')
        inputanSuhu = float(input('\nMasukkan suhu dalam satuan Fahrenheit: '))
        kelvinToCelcius(fahrenheitToKelvin(inputanSuhu))
    elif inputMenu == '2':
        os.system('cls')
        print('================== Menu Perhitungan dari Fahrenheit ke Celcius ==================\n')
        inputanSuhu = float(input('Masukkan suhu dalam satuan Fahrenheit: '))
        celciusToKelvin(fahrenheitToCelcius(inputanSuhu))

def fahrenheitToKelvin(inputanSuhu):
    ''' Konversi dari Fahrenheit ke Kelvin '''
    konversi = (inputanSuhu-32) * 5 / 9 + 273.15
    konversiFormat = math.floor(konversi*100000)/100000
    konversiInteger = math.floor(konversi)
    suhuFormat = math.floor(inputanSuhu*100000)/100000
    suhuInteger = math.floor(inputanSuhu)    
    if ((inputanSuhu % 1 != 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Fahrenheit adalah {konversiFormat} derajat Kelvin')
    elif((inputanSuhu % 1 != 0) and (konversi % 1 == 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Fahrenheit adalah {konversiInteger} derajat Kelvin')
    elif((inputanSuhu % 1 == 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Fahrenheit adalah {konversiFormat} derajat Kelvin')
    else:
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Fahrenheit adalah {konversiInteger} derajat Kelvin') 
    return konversi

def fahrenheitToCelcius(inputanSuhu):
    ''' Konversi dari Fahrenheit ke Celcius '''
    konversi = (inputanSuhu-32) * 5 / 9
    konversiFormat = math.floor(konversi*100000)/100000
    konversiInteger = math.floor(konversi)
    suhuFormat = math.floor(inputanSuhu*100000)/100000
    suhuInteger = math.floor(inputanSuhu)    
    if ((inputanSuhu % 1 != 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Fahrenheit adalah {konversiFormat} derajat Celcius')
    elif((inputanSuhu % 1 != 0) and (konversi % 1 == 0)):
        print(f'\n=> Konversi suhu dari {suhuFormat} derajat Fahrenheit adalah {konversiInteger} derajat Celcius')
    elif((inputanSuhu % 1 == 0) and (konversi % 1 != 0)):
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Fahrenheit adalah {konversiFormat} derajat Celcius')
    else:
        print(f'\n=> Konversi suhu dari {suhuInteger} derajat Fahrenheit adalah {konversiInteger} derajat Celcius') 
    return konversi

def menuUtama():
    ''' Menu Utama '''
    os.system('cls')
    print('Username dan password yang Anda masukkan benar!\n')
    while True:
        templateMenuUtama()
        inputMenu = (input('\nMasukkan pilihan menu yang diinginkan (1 - 5): '))
        while inputMenu not in ['1','2','3','4','5']:
            os.system('cls')
            print("Inputan yang Anda masukkan salah! Mohon untuk input menu yang ditampilkan....\n")
            templateMenuUtama()
            inputMenu = (input("\nMohon untuk memasukkan pilihan menu yang diinginkan (1 sampai 7): ")) 
        if inputMenu == '1':
            tempKelvinCelcius()
        elif inputMenu == '2':
            tempOthersToFahrenheit()
        elif inputMenu == '3':
            tempFahrenheitToOthers()
        elif inputMenu == '4':
            os.system('cls')
            about()
        elif inputMenu == '5':
            os.system('cls')
            keluarProgram()
        opsiBalikKeMenu = input("\nApakah ingin kembali ke menu utama? (Y or N) : ")
        while (opsiBalikKeMenu not in opsiMenu):
            os.system('cls')
            print('Inputan yang Anda masukan salah! Mohon untuk memasukkan inputan sesuai perintah di menu...\n')
            opsiBalikKeMenu = input("Apakah ingin kembali ke menu utama? (Y or N) : ")
        if (opsiBalikKeMenu in ['No','N','no','n']):
            keluarProgram()
        else:
            os.system('cls')
            continue                    

if __name__ == "__main__":
    os.system('cls')
    username = input('Masukkan username (dean): ')
    password = input('Masukkan password (dean123): ')
    if (username==user and password==pwd):
        menuUtama()
    else:
        salahUserOrPass()