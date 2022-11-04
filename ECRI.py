import time # make delays
import os # for work with shell
print('Welcome to the ECRI (Easy Custom Recovery Installer)')
print('''
########## ########## ####### #######
#          #          #     #    #
#          #          #     #    #
########## #          #######    #
#          #          # #        #
#          #          #  #       #
########## ########## #   ### ####### (4pda.to, Vankinok, https://4pda.to/forum/index.php?showuser=9457591)
''')
print('Put the recovery.img to the folder with ECRI')
time.sleep(2)
os.system("fastboot.exe getvar product") # product: alioth (for example)
var = input('''What is your partition table(a-only - ao, ab - ab)?
: ''')
if var == "ao":
    print('Chose: A-only, you have got recovery partition')
    print('')
    input('''
    ''')
    print('')
    os.system("dir")
    print('')
    var1 = input('''Are you ready flash the image? (y/n)
    : ''')
    print('')
    if var1 == n:
        exit(0)
    if var1 == y:
        os.system("fastboot.exe flash recovery recovery.img") # flashing the recovery image
        print('')
        os.system("fastboot.exe reboot recovery") # rebooting to the recovery
        print('')
        input("Press enter to exit, see you soon choom: ")
if var == "ab":
    print('''
    Chose: AB partition table, you haven't recovery partition, 
    it means the recovery live in boot partititon (in ramdisk)
    ''')
    print('')
    os.system("dir")
    print('')
    var2 = input('''Are you ready boot into the temporary recovery? (y/n)
    : ''')
    print('')
    if var2 == "n":
        exit(0)
    if var2 == "y":
        print('')
        os.system("fastboot.exe boot recovery.img") # booting to the temporary recovery
        print('')
        print('Do not disconnect your phone from computer!!!')
        print('')
        os.system("adb.exe wait-for-device") # waiting the device         
        print('')
        os.system("adb.exe push MFP-STABLE-4.1.11.zip /sdcard") # putting .zip into the storage
        print('')
        os.system("adb.exe push recovery.img /sdcard") # putting recovery image into the storage
        print('')
        os.system("adb.exe shell twrp install /sdcard/MFP-STABLE-4.1.11.zip") # Thanks LeeGarChat for this cool script
        print('')
        os.system("adb.exe shell rm -rf /sdcard/MFPLOGS") # deleting the logs
        print('')
        os.system("adb.exe shell rm -rf /sdcard/MFP-STABLE-4.1.11.zip") # deleting the .zip
        print('')
        os.system("adb.exe shell rm -rf /sdcard/recovery.img") # deleting the boot image
        print('')
        input('Press enter to exit, see you soon choom: ') # goodbye
        # Happy pythoning!
