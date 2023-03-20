# Créer par Exa
import os
import pystyle
from pystyle import Colors, Colorate
import time
from datetime import datetime
x = 0 # -- Ne pas changer

while x != 1: # -- Boucle infini
    os.system("TASKKILL /F /IM QAppTray.exe /T") # -- Arrêt de Qstudio
    print(Colorate.Diagonal(Colors.rainbow, 'Programme executer le : ', 2), datetime.now()) # -- Vous pouvez changer le text
    time.sleep(0.5) # -- Ne pas changer
