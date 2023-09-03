import os
import time
import shutil

source = '/chemin/vers/votre/dossier'
destination = '/chemin/vers/votre/dossier_de_sauvegarde'

frequence_sauvegarde = 5 * 60

timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
dossier_sauvegarde = f'sauvegarde_{timestamp}'
chemin_dossier_sauvegarde = os.path.join(destination, dossier_sauvegarde)

# Vérifie si le dossier de sauvegarde existe déjà
if not os.path.exists(chemin_dossier_sauvegarde):
    # S'il n'existe pas, alors copiez le contenu du dossier source vers le dossier de sauvegarde
    shutil.copytree(source, chemin_dossier_sauvegarde)

time.sleep(frequence_sauvegarde)

print("Terminé")
