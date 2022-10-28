import time
import os
print('Добро пожаловать в ECRI (Easy Custom Recovery Installer)')
print('''
########## ########## ####### #######
#          #          #     #    #
#          #          #     #    #
########## #          #######    #
#          #          # #        #
#          #          #  #       #
########## ########## #   ### ####### (4pda.to, Vankinok, https://4pda.to/forum/index.php?showuser=9457591)
''')
os.system("fastboot.exe getvar product")
var = input('''У вас таблица разделов A-only(ao) или AB(ab)?
: ''')
if var == "ao":
    print('Выбрано: A-only, следовательно у вас есть раздел recovery')
    print('')
    input('''Теперь поместите образ рекавери с именем recovery.img под ваше устройство в папку с ECRI.exe, а после нажмите enter
    ''')
    print('')
    os.system("dir")
    print('')
    var1 = input('''Вы готовы к прошивке образа? (y/n)
    : ''')
    print('')
    if var1 == n:
        exit(0)
    if var1 == y:
        os.system("fastboot.exe flash recovery recovery.img")
        print('')
        os.system("fastboot.exe reboot recovery")
        print('')
        input("Нажмите enter, чтобы выйти: ")
if var == "ab":
    print('''
    Выбрано: AB, следовательно у вас нет раздела recovery, 
    а это значит, что рекавери находится в boot образе (в ramdisk)
    ''')
    print('')
    input('Теперь поместите образ рекавери с именем recovery.img под ваше устройство в папку с ECRI.exe, а после нажмите enter: ')
    print('')
    os.system("dir")
    print('')
    var2 = input('''Вы готовы к запуску во временное рекавери? (y/n)
    : ''')
    print('')
    if var2 == "n":
        exit(0)
    if var2 == "y":
        print('')
        os.system("fastboot.exe boot recovery.img")
        print('')
        print('Не отключайте телефон от пк!!!')
        print('')
        time.sleep(2)
        input('Когда телефон будет запущен в рекавери, то нажмите enter')
        var22 = input('''
        У вас дата зашифрована? Если не знаете пароль или рекавери не умеет работать
        с шифрованием вашей версией андроид, то необходимо сделать format data.
        Хотите сделать format data? (y/n)
        : 
        ''')
        if var22 == "n":
            print('')
            os.system("adb.exe devices")
            print('')
            input('''
            Телефон определился? Если нет, то убедитесь, 
            что компьютер видит телефон, если все ок, то нажмите enter: ''')            
            print('')
            os.system("adb.exe push MFP-STABLE-4.1.11.zip /sdcard")
            print('')
            os.system("adb.exe push recovery.img /sdcard")
            print('')
            os.system("adb.exe shell twrp install /sdcard/MFP-STABLE-4.1.11.zip")
            print('')
            os.system("adb.exe shell rm -rf /sdcard/MFPLOGS")
            print('')
            os.system("adb.exe shell rm -rf /sdcard/MFP-STABLE-4.1.11.zip")
            print('')
            os.system("adb.exe shell rm -rf /sdcard/recovery.img")
            print('')
            input('Нажмите enter, чтобы выйти: ') 
        if var22 == "y":
            os.system("adb.exe shell twrp format data")
            print('')
            os.system("adb.exe reboot bootloader")
            print('')
            os.system("fastboot.exe boot recovery.img")
            print('')
            print('Не отключайте телефон от пк!!!')
            print('')
            time.sleep(2)
            input('Когда телефон будет запущен в рекавери, то нажмите enter')
            print('')
            os.system("adb.exe devices")
            print('')
            input('''
            Телефон определился? Если нет, то убедитесь, 
            что компьютер видит телефон, если все ок, то нажмите enter: ''')
            os.system("adb.exe push MFP-STABLE-4.1.11.zip /sdcard")
            print('')
            os.system("adb.exe push recovery.img /sdcard")
            print('')
            os.system("adb.exe shell twrp install /sdcard/MFP-STABLE-4.1.11.zip")
            print('')
            os.system("adb.exe shell rm -rf /sdcard/MFPLOGS")
            print('')
            os.system("adb.exe shell rm -rf /sdcard/MFP-STABLE-4.1.11.zip")
            print('')
            os.system("adb.exe shell rm -rf /sdcard/recovery.img")
            print('')
            input('Нажмите enter, чтобы выйти: ')       