import os
import string

os.system('cls')
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949
  ]
username = input('Masukkan username (dean): ')
password = input('Masukkan password (dean123): ')
user = 'dean'
pwd = 'dean123'
angka = ['1','2','3','4','5','6','7','8','9','0']

opsiMenu = ['No','N','no','n', 'yes','Yes', 'y', 'Y']
# balikKeMenu = ['yes','Yes', 'y', 'Y']
if (username==user and password==pwd):
    os.system('cls')
    print('Username dan password yang Anda masukkan benar!\n')
    while True:
        print('================== Selamat datang di program untuk Assignment 1 Python Flask ==================\n')
        # print("Nama lengkap saya : Deandri Firdaus")
        # print("Nomor peserta saya : FSDO002ONL013")
        # print("Alamat saya : Jakarta Selatan\n")
        print("Menu Soal: ")
        print("1. Assignment 1")
        print("2. Assignment 1 Updated")
        print("3. Assignment 1 dengan Inputan")
        print("4. Soal Factorial")
        print("5. Piramida Alfabet")
        # print("5. Soal Number to String")
        print("6. About")
        print("7. Exit")
        inputMenu = (input('\nMasukkan pilihan menu yang diinginkan (1 - 7): '))
        while inputMenu not in ['1','2','3','4','5','6','7']:
            os.system('cls')
            print("Inputan yang Anda masukkan salah! Mohon untuk input menu yang ditampilkan....\n")
            print('================== Selamat datang di program untuk Assignment 1 Python Flask ==================\n')
            print("Menu Soal: ")
            print("1. Assignment 1")
            print("2. Assignment 1 Updated")
            print("3. Assignment 1 dengan Inputan")
            print("4. Soal Factorial")
            print("5. Piramida Alfabet")
            # print("5. Soal Number to String")
            print("6. About")
            print("7. Exit")
            inputMenu = (input("\nMohon untuk memasukkan pilihan menu yang diinginkan (1 sampai 7): "))

        if inputMenu == '1':
            os.system('cls')
            print('================== Ini adalah menu Assignment 1 ==================\n')
            print('Kumpulan list adalah....')
            print(numbers)
            print('\nSoal: Loop dan print semua angka genap dari list angka diatas dengan urutan yang sama. Jangan mencetak angka apa pun yang muncul setelah angka 918.')
            print('\nJawabannya adalah sebagai berikut....')
            for i in numbers:
                if i==918:
                    print(i, "Looping-berakhir")
                    break
                else:
                    if(i%2==0):
                        print(i, end=" ")
                    else:
                        continue
        elif inputMenu == '2':
            os.system('cls')
            print('================== Ini adalah menu Assignment 1 Updated ==================\n')
            nilaiGenap = filter(lambda x: x % 2 == 0, numbers)
            nilaiGanjil = filter(lambda x: x % 2 != 0, numbers)
            listFilteredGenap = list(nilaiGenap)
            listFilteredGanjil = list(nilaiGanjil)
            sortAscending = sorted(numbers, key=int)
            sortDescending = sorted(numbers, key=int, reverse=True)
            sortAscendingGenap = sorted(listFilteredGenap, key=int)
            sortAscendingGanjil = sorted(listFilteredGanjil, key=int)
            sortDescendingGenap = sorted(listFilteredGenap, key=int, reverse=True)
            sortDescendingGanjil = sorted(listFilteredGanjil, key=int, reverse=True)
            print('\nKumpulan baris genap dari list adalah....')
            print(listFilteredGenap)
            print('\nKumpulan baris ganjil dari list adalah....')
            print(listFilteredGanjil)
            print('\nKumpulan list yang telah disortir Ascending adalah....')
            print(sortAscending)
            print('\nKumpulan list yang telah disortir Ascending Genap adalah....')
            print(sortAscendingGenap)
            print('\nKumpulan list yang telah disortir Ascending Ganjil adalah....')
            print(sortAscendingGanjil)
            print('\nKumpulan list yang telah disortir Descending adalah....')
            print(sortDescending)
            print('\nKumpulan list yang telah disortir Descending Genap adalah....')
            print(sortDescendingGenap)
            print('\nKumpulan list yang telah disortir Descending Ganjil adalah....')
            print(sortDescendingGanjil)
        elif inputMenu == '3':
            os.system('cls')
            print('================== Ini adalah menu Assignment 1 Dengan Inputan ==================\n')
            listInput = []
            inputElemen = int(input("\nMasukkan banyaknya elemen dalam list (number or integer only) : "))
            
            # iterating till the range
            for i in range(0, inputElemen):
                a = i+1
                elemen = input(f'Masukkan elemen ke-{a}: ')
                if any(elemen in s for s in angka):
                    elementInteger = int(elemen)
                    listInput.append(elementInteger) # adding the element
                else:
                    listInput.append(elemen) # adding the element 
            print(f"\nList yang telah dibuat adalah = {listInput}")
            
            # user input nilai yang ingin dihapus, kita cari indexnya, hapus nilainya
            inputElemenDihapus = input("\nMasukkan nilai elemen yang ingin dihapus dalam list : ")
            if any(inputElemenDihapus in s for s in angka):
                inputElemenDihapusInteger = int(inputElemenDihapus)
                indexElemenDihapus = listInput.index(inputElemenDihapusInteger)
            else:
                indexElemenDihapus = listInput.index(inputElemenDihapus)
            print(f'Index elemen yang ingin dihapus adalah index ke-{indexElemenDihapus}')
            del listInput[indexElemenDihapus]
            print(f"List baru yang telah dihapus salah satu elemennya = {listInput}")

            # user tambah 1 elemen di ujung
            inputElemenBaruTerakhir = input("\nMasukkan nilai elemen yang ingin ditambahkan di akhir list : ")
            if any(inputElemenBaruTerakhir in s for s in angka):
                inputElemenBaruTerakhirInteger = int(inputElemenBaruTerakhir)
                listInput.append(inputElemenBaruTerakhirInteger) # adding the element
            else:
                listInput.append(inputElemenBaruTerakhir) # adding the element
            print(f"List baru yang telah ditambahkan satu elemen baru di ujung list = {listInput}")

            # user tambah 1 elemen di posisi yang diinginkan
            inputElemenBaruSesuaiIndex = input("\nMasukkan nilai elemen yang ingin ditambahkan di list : ")
            inputPosisiElemen = int(input("Masukkan posisi yang diinginkan untuk elemen tersebut di dalam list (number or integer only) : "))
            indexPosisiElemen = inputPosisiElemen - 1
            if any(inputElemenBaruSesuaiIndex in s for s in angka):
                inputElemenBaruSesuaiIndexInteger = int(inputElemenBaruSesuaiIndex)
                listInput.insert(indexPosisiElemen,inputElemenBaruSesuaiIndexInteger)
            else:
                listInput.insert(indexPosisiElemen,inputElemenBaruSesuaiIndex)
            print(f"List baru yang telah ditambahkan satu elemen baru di ujung list = {listInput}")

            # reverse list
            listInput.reverse()
            print(f"\nList baru yang telah diputar urutannya = {listInput}")

        elif inputMenu == '4':
            os.system('cls')
            faktorial = 1
            print('================== Ini adalah menu Factorial ==================\n')
            angkaFaktorial = int(input("Masukkan angka faktorial yang diinginkan (number atau integer only): "))
            if(angkaFaktorial==0):
                print(f'\nHasil faktorial dari angka {angkaFaktorial} adalah {faktorial}')
            elif(angkaFaktorial>0):
                for i in range(1,angkaFaktorial+1):
                    faktorial = faktorial * i
                print(f'\nHasil faktorial dari angka {angkaFaktorial} adalah {faktorial}')
        elif inputMenu == '5':
            os.system('cls')
            print('================== Ini adalah menu Piramida Alfabet ==================\n')
            baris = int(input("Masukkan banyak baris yang diinginkan dan maksimal 26 baris (number atau integer only): "))
            alphabet = string.ascii_uppercase
            alphabetList = list(alphabet)
            for i in range (1,baris+1):
                for j in range (baris,i,-1):
                    print(" ", end="")
                for k in range (0,i):
                    print(alphabetList[k], end="")
                l = 1
                m = (i - 1) - l
                while (m >= 0):
                    print(alphabetList[m], end="")
                    m-=1
                l+=1
                print('')          
        elif inputMenu == '6':
            os.system('cls')
            print('================== Ini adalah menu About ==================\n')
            print("Nama lengkap saya : Deandri Firdaus")
            print("Nomor peserta saya : FSDO002ONL013")
            print("Alamat saya : Jakarta Selatan\n")
        elif inputMenu == '7':
            os.system('cls')
            print('\n**************************************')
            print('**************************************')
            print('\nAnda memilih untuk keluar dari program')
            print('\n**************************************')
            print('**************************************')
            print('\n\tProgram akan ditutup\n')
            quit()   
            
        opsiBalikKeMenu = input("\nApakah ingin kembali ke menu utama? (Y or N) : ")
        while (opsiBalikKeMenu not in opsiMenu):
            os.system('cls')
            print('Inputan yang Anda masukan salah! Mohon untuk memasukkan inputan sesuai perintah di menu...\n')
            opsiBalikKeMenu = input("Apakah ingin kembali ke menu utama? (Y or N) : ")
        if (opsiBalikKeMenu in ['No','N','no','n']):
            os.system('cls')
            print('\n**************************************')
            print('**************************************')
            print('\nAnda memilih untuk keluar dari program')
            print('\n**************************************')
            print('**************************************')
            print('\n\tProgram akan ditutup\n')
            quit()
        else:
            os.system('cls')
            continue    

else:
    os.system('cls')
    print('\n***********************************************')
    print('***********************************************')
    print('\nUsername atau password yang Anda masukan salah!')
    print('\n***********************************************')
    print('***********************************************')
    print('\n\t    Program akan ditutup\n')
    quit()   