import random
from scapy.all import *
import time
from colorama import Fore, Style
import itertools

user_confirmation = False

usages = {
    '0': 'Exit',
    '1': 'DDoS Attack',
    '2': 'Brute Force Generator',
    '3': 'Cross-Site Scripting',
    '4': 'Phishing Attack',
    '5': 'Man-in-the-Middle (MitM) Attack',
    '6': 'SQL Injection',
    '7': 'Social Engineering',
    '8': 'Keylogger',
    '9': 'Ransomware',
    '10': 'Cryptojacking',
    '11': 'Botnet',
    '12': 'Trojan',
    '13': 'Virus',
    '14': 'Worm',
    '15': 'Rootkit',
    '16': 'Spyware',
    '17': 'Backdoor',
    '18': 'Logic Bomb',
    '19': 'Fileless Malware',
    '20': 'Adware',
    '21': 'Malvertising',
    '22': 'Phishing',
    '23': 'Spear Phishing',
    '24': 'Whaling',
    '25': 'Vishing',
    '26': 'Smishing',
    '27': 'Pharming',
    '28': 'Watering Hole Attack',
    '29': 'DNS Spoofing',
    '30': 'Session Hijacking',
    '31': 'Cookie Theft',
    '32': 'Clickjacking',
    '33': 'Eavesdropping',
    '34': 'Baiting',
    '35': 'Quid Pro Quo',
    '36': 'Tailgating',
    '37': 'Pretexting',
    '38': 'Scareware',
    '39': 'Antivirus Evasion',
    '40': 'Exploit Kit',
    '41': 'Zero-Day Exploit',
    '42': 'Drive-By Download',
    '43': 'Malware',
    '44': 'Trojan Horse',
    '45': 'Logic Bomb',
    '46': 'Backdoor',
    '47': 'Bot',
    '48': 'Ransomware',
    '49': 'Rootkit',
    '50': 'Spyware',
    '51': 'Adware',
    '52': 'Worm',
    '53': 'Virus',
    '54': 'Fileless Malware',
    '55': 'Keylogger',
    '56': 'Cryptojacking'
}


def get_usage():
    global user_input
    global usage
    global user_confirmation

    if user_confirmation == False:
        user_confirmation_input = input("I have read the disclaimer and agree to use this program on my own network. (y/n): ")
        if user_confirmation_input == "y":
            user_confirmation = True
            user_input = input("Enter a number (0-56) to start a attack: ")
            usage = usages.get(user_input, "Invalid input")
            if usage == "Invalid input":
                print(Fore.RED + "Invalid input")
                get_usage()
        elif user_confirmation_input == "n":
            user_confirmation = False
            print("Exiting...")
            time.sleep(2)
            exit()
        else:
            user_confirmation = False
            print(Fore.RED + "Invalid input")
            get_usage()

    user_input = input("Enter a number (0-56) to start a attack: ")
    usage = usages.get(user_input, "Invalid input")


def bruteforcegen():
    num_chars = int(input("Enter number of characters to brute force: "))

    with open('brute_force_output.txt', 'w') as f:
        for combination in brute_force(num_chars):
            f.write(combination + '\n')

    print("All combinations saved to brute_force_output.txt")


def brute_force(num_chars):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return (''.join(i) for i in itertools.product(characters, repeat=num_chars))


text = '''
             .______   .______          ___       __  .__   __.  _______   ______   .______        ______  _______ 
             |   _  \  |   _  \        /   \     |  | |  \ |  | |   ____| /  __  \  |   _  \      /      ||   ____|
             |  |_)  | |  |_)  |      /  ^  \    |  | |   \|  | |  |__   |  |  |  | |  |_)  |    |  ,----'|  |__   
             |   _  <  |      /      /  /_\  \   |  | |  . `  | |   __|  |  |  |  | |      /     |  |     |   __|  
             |  |_)  | |  |\  \----./  _____  \  |  | |  |\   | |  |     |  `--'  | |  |\  \----.|  `----.|  |____ 
             |______/  | _| `._____/__/     \__\ |__| |__| \__| |__|      \______/  | _| `._____| \______||_______|
                                                                                                       

______________________________________________________________________________________________________________________________________
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
[0] - Exit                   [14] - Worm                   [28] - Watering Hole Attack  [42] - Drive-By Download  [56] - Cryptojacking
[1] - DDoS Attack            [15] - Rootkit                [29] - DNS Spoofing          [43] - Malware
[2] - Brute Force Generator  [16] - Spyware                [30] - Session Hijacking     [44] - Trojan Horse
[3] - Cross-Site Scripting   [17] - Backdoor               [31] - Cookie Theft          [45] - Logic Bomb
[4] - Phishing Attack        [18] - Logic Bomb             [32] - Clickjacking          [46] - Backdoor
[5] - Man-in-the-Middle      [19] - Fileless Malware       [33] - Eavesdropping         [47] - Bot
[6] - SQL Injection          [20] - Adware                 [34] - Baiting               [48] - Ransomware
[7] - Social Engineering     [21] - Malvertising           [35] - Quid Pro Quo          [49] - Rootkit
[8] - Keylogger              [22] - Phishing               [36] - Tailgating            [50] - Spyware
[9] - Ransomware             [23] - Spear Phishing         [37] - Pretexting            [51] - Adware
[10] - Cryptojacking         [24] - Whaling                [38] - Scareware             [52] - Worm
[11] - Botnet                [25] - Vishing                [39] - Antivirus Evasion     [53] - Virus
[12] - Trojan                [26] - Smishing               [40] - Exploit Kit           [54] - Fileless Malware
[13] - Virus                 [27] - Pharming               [41] - Zero-Day Exploit      [55] - Keylogger        

**DISCLAIMER**: We are not responsible for any damage caused by the program. Use it solely on your own network and at your own risk!
'''



print(Fore.RED)
for char in text:
    print(char, end='')
    time.sleep(0.001)



get_usage()
print(Fore.GREEN + "[USAGE]:", usage)