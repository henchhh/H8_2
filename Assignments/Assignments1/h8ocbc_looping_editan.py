import os
os.system('cls')
print('\n======================== PROGRAM PRINT ANGKA GENAP SAMPAI 918 PADA LIST ========================\n')
username = input('Masukkan username (dean): ')
password = input('Masukkan password (dean123): ')
user = 'dean'
pwd = 'dean123'
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949
  ]
if (username==user and password==pwd):
  os.system('cls')
  print('\nUsername dan password yang Anda masukkan benar!')
  print('=== Selamat datang di program untuk Assignment 1 Python Flask ===')
  print("Nama lengkap saya : Deandri Firdaus")
  print("Nomor peserta saya : FSDO002ONL013")
  print("Alamat saya : Jakarta Selatan")
  print("Menu Soal: ")
  print("1. Assignment 1")
  print("2. Assignment 1 Updated")
  print("3. Soal Factorial")
  print("4. Soal Reversed Number")
  print("5. Soal Number to String")
  print("6. About / Tentang Saya")
  print("7. Exit")
  inputMenu = int(input('Masukkan pilihan menu yang diinginkan (1 sampai 7): '))
  while inputMenu < 1 or inputMenu > 4:
        print("The selection provided is invalid.")
        inputMenu = int(input("Mohon untuk memasukkan pilihan menu yang diinginkan (1 sampai 7): "))

    if inputMenu == 1:
        rules()
    elif inputMenu == 2:
        onePlayer()
    elif inputMenu == 3:
        twoPlayer()
    elif inputMenu == 4:
        endGame()

  

  print('\n======================== PROGRAM PRINT ANGKA GENAP SAMPAI 918 PADA LIST ========================\n')
  print('Angka-angka yang akan ditampilkan adalah sebagai berikut:\n')
  for i in numbers:
      if i==918:
        print(i, "Looping-berakhir")
        break
      else:
        if(i%2==0):
          print(i, end=" ")
        else:
          continue
else:
  os.system('cls')
  print('********')
  print('********')
  print('********')
  print('\nUsername atau password yang Anda masukan salah!')
  print('\n********')
  print('********')
  print('********')
  print('\nProgram akan ditutup')
  quit()        
      # if(i%2==0):
      #   print(i)
      # else:
      #   continue

# print('')  
# for i in numbers:
#   while(i!=918):
#     if(i%2==0):
#       print (i, end=" ")
#       break
#     else:
#       break
#   else:
#     print(i,'\nDone')
#     break


 
# number of elements as input
print("\n=============== PROGRAM LIST INPUTAN USER =================")
listInput = []
inputElemen = int(input("\nMasukkan banyaknya elemen dalam list : "))
 
# iterating till the range
for i in range(0, inputElemen):
  a = i+1
  elemen = int(input(f'Masukkan elemen ke-{a}: '))
 
  listInput.append(elemen) # adding the element

print(f"\nList yang telah dibuat adalah = {listInput}")

# Menghapus index yang diinginkan
inputIndex = int(input("\nMasukkan index yang ingin dihapus dalam list : "))
del listInput[inputIndex]
print(f"\nList setelah elemen yang diinginkan dihapus adalah = {listInput}")


#Menampilkan nilai genap dan nilai ganjil
nilaiGenap = filter(lambda x: x % 2 == 0, listInput)
nilaiGanjil = filter(lambda x: x % 2 != 0, listInput)
listFilteredGenap = list(nilaiGenap)
listFilteredGanjil = list(nilaiGanjil)
print(f"List elemen genap adalah = {listFilteredGenap}")
print(f"List elemen ganjil adalah = {listFilteredGanjil}")

# Menghapus nilai elemen yang diinginkan
inputElemenDihapus = int(input("\nMasukkan nilai elemen yang ingin dihapus dalam list : "))
indexElemenDihapus = listInput.index(inputElemenDihapus)
print(f'Index elemen yang ingin dihapus adalah index ke-{indexElemenDihapus}')
# del listInput[inputElemenTerakhir]
# print(f"\nList setelah elemen yang diinginkan dihapus adalah = {listInput}")

#Menampilkan nilai genap dan nilai ganjil
nilaiGenap = filter(lambda x: x % 2 == 0, listInput)
nilaiGanjil = filter(lambda x: x % 2 != 0, listInput)
listFilteredGenap = list(nilaiGenap)
listFilteredGanjil = list(nilaiGanjil)
print(f"\nList elemen genap adalah = {listFilteredGenap}")
print(f"List elemen ganjil adalah = {listFilteredGanjil}")


# for i in listInput:
#   while(listInput[i]!=listInput[inputElemenTerakhir]):
#       print (i, end=" ")
#       break



# next(x for x in lst if ...)

# [i for i,x in enumerate([1,2,3,2]) if x==2]

# n = int(input("\nMasukkan elemen terakhir yang ingin ditampilkan : "))



