#---------------------------------------------------------------------------#
# Fonctions générales pour le  reste du package
#---------------------------------------------------------------------------#

import os

#createFolder : crée un Folder à new_path
#Increment détermine si une incrémentation doit être ajouté dans le cas
#ou new_path existe déjà

def createFolder(new_path,increment=False):
    if increment:
        i = 0
        test_path = new_path
        while os.path.exists(test_path):
            i += 1
            test_path = new_path + str(i)
        os.makedirs(test_path)
        return test_path
    else:
        try:
            if not os.path.exists(new_path):
                os.makedirs(new_path)
        except OSError:
            print('The directory ' + new_path + ' already exists.')
        return new_path
