import sqlite3
import psutil
import os

# OS utilisé => nt = windows
print(os.name)

print(" ____ ")
print("\  _`\                        __                    ")
print(" \ \L\ \ _ __   ___     ___  /\_\   ____    ____    ")
print("  \ \ ,__//\`'__\/ __`\ /' _ `\\/\ \ /\_ ,`\ /\_ ,`\  ")
print("   \ \ \/ \ \ \//\ \L\ \/\ \/\ \\ \ \\/_/  /_\/_/  /_ ")
print("    \ \_\  \ \_\\ \____/\ \_\ \_\\ \_\ /\____\ /\____\ ")
print("     \/_/   \/_/ \/___/  \/_/\/_/ \/_/ \/____/ \/____/")
print("")

def if_process_is_running_by_exename(exename):

    for proc in psutil.process_iter(['pid', 'name']):
        #print(proc.info)
        # Check si le programme recherché est en cours d'exécution
        if proc.info['name'] == exename:
            return True
    return False


chromeRunning = if_process_is_running_by_exename('mozilla.exe')

if chromeRunning:
    con = sqlite3.connect('C:\\Users\\Dumhuzy\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
    cursor = con.cursor()
    cursor.execute("SELECT url FROM urls")
    urls = cursor.fetchall()
    print('\n'.join(urls))
else:
    print('! Chrome est dèja ouvert, impossible de récupérer l\'historique')
    userResponse = input('=> Voulez-vous fermer chrome Y/N ?')

    if userResponse == 'N' or userResponse == 'n':
        print('== Abandon du processus ==')
    elif userResponse == 'Y' or userResponse == 'y':
        print('Nous allons fermer chrome')
    else:
        print('== Mauvais choix, abandon du processus ==')

