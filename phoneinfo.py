import os
import time
import sys
import colorama
from colorama import Fore
import phonenumbers
from phonenumbers import geocoder, carrier,timezone,util
import platform
import httplib
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#########################
versionPath = "core"+os.sep+"version.txt"
user = platform.system()
def updatephoneinfo():
    if not os.path.isfile(versionPath):
        errMsg("Unable to check for updates: please re-clone the script to fix this problem")
        sys.exit(1)
        write("[~] Checking for updates...\n")
        conn = httplib.HTTPSConnection("raw.githubusercontent.com")
        conn.request("GET", "/FonderElite/Phone-Info/master/core/version.txt")
        repoVersion = conn.getresponse().read().strip().decode()
    with open(versionPath) as vf:
        currentVersion = vf.read().strip()
    if repoVersion == currentVersion:
        write("  [*] The script is up to date!\n")
    else:
        print("  [+] An update has been found ::: Updating... ")
        conn.request("GET", "/FonderElite/Phone-Info/master/phoneinfo.py")
        newCode = conn.getresponse().read().strip().decode()
    with open("phoneinfo.py", "w") as  phoneinfo:
        phoneinfo.write(newCode)
    with open(versionPath, "w") as ver:
        ver.write(repoVersion)
        write("  [+] Successfully updated :)\n")
        sys.exit()

def helpm():
            print(Fore.GREEN + '''
=============================================
+|  Phone-Info  By  F o n d e r E l i t e  |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -p         PhoneNumber             |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex. ./phoneinfo -p -s                    |+
+|=========================================|+
''')
banner = (Fore.GREEN+ '''
  __i
|---|    
|[_]|   Phone-Number Information
|:::|    Gathering Tool
|:::|    
`\   \   
  \_=_\                                 
    ''')
social = Fore.MAGENTA + '''
 Made By FonderElite || Droid
 Visit My Github Page: https://github.com/Fonderelite
 '''
help = Fore.GREEN + '''
=============================================
+|  Phone-Info  By  F o n d e r E l i t e  |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -p         PhoneNumber             |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex. ./phoneinfo -p -s (InfoGathering)    |+
+|=========================================|+
'''
btcadd = Fore.MAGENTA + 'bc1q5v7p34qsghjyzv8dc7n8egkuz80kc5xw38n7yn'
print(banner)
time.sleep(2)
print(social)
print(help)
print(Fore.YELLOW + 
'Support me by donating in my bitcoin wallet:' + Fore.BLUE + btcadd)
while True:
 command = input(wi + gr + "[+]Input a command: ")
 if command == "./phoneinfo -h":
    print(help)
 elif command == "./phoneinfo -p -s":
     phonenum = input("Input a Phone Number to start: ")
     phone_number = phonenumbers.parse(phonenum)
     validate = phonenumbers.is_valid_number(phone_number)
     location = geocoder.country_name_for_number(phone_number,'en')
     region = geocoder.description_for_number(phone_number,'en')
     probability = phonenumbers.is_possible_number(phone_number)
     metadata = phonenumbers.PhoneMetadata(phone_number)
     carrier_desc = carrier.name_for_number(phone_number,'en')
     timezone = timezone.time_zones_for_number(phone_number)
     source = phonenumbers.PhoneNumberDesc(phone_number)
     str(validate)
     print(Fore.MAGENTA + "Checking if Phone Number is Valid...")
     time.sleep(2)
     print(Fore.CYAN + str(validate))
     time.sleep(1)
     print(Fore.MAGENTA + "Location: " + Fore.CYAN + location)
     time.sleep(1)
     print(Fore.MAGENTA + "Probability(If False): " + Fore.CYAN + str(probability))
     time.sleep(1)
     print(Fore.MAGENTA + "Metadata: " + Fore.CYAN + str(metadata))
     time.sleep(1)
     print(Fore.MAGENTA + "Carrier: " + Fore.CYAN + carrier_desc)
     time.sleep(1)
     print(Fore.MAGENTA + "Timezone: " + Fore.CYAN + str(timezone))
     time.sleep(1)
     print(Fore.MAGENTA + "Description: " + Fore.CYAN + str(source))
 elif command == "./phoneinfo -u":
     updatephoneinfo()
 elif command == "./phoneinfo -q":
  print(Fore.RED + "(っ◔◡◔)っ ♥ Quitting.... ♥")
  break

 else:
     print(Fore.RED + '''
___  __   __   __    __ 
|__  |__) |__) /  \ |__)    
|___ |  \ |  \ \__/ |  \    
                          
     ''')
time.sleep(0.2)
sys.exit()


