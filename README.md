# Exec\_briaree
> Fichier contenant des executables a utiliser sur Briaree

Les executables sont dans le fichier bin/.

aclocal-1.\* et automake-1.\* sont des liens symboliques (fonctionne seulement sur Briaree)

createpbs.py: crée des fichiers de soumission de tache

enlarge.py: prend un fichier position et l'agrandie (fonctionne pour les cellules de graphene générée avec le package functions\_briaree)

rename.py: etape intermediaire pour les calculs NEB

restart\_NEB.py: relance un calcul NEB en gardant la progression du premier

translation.py: translate un fichier position


## Installation

A ajouter au ~/.bashrc:
```sh
export PATH="PATH_TO_INSTALLATION/exec_briaree/bin:$PATH"
```

## Requirements

Le package python [functions\_briaree](https://github.com/OMalenfantThuot/functions_briaree) doit etre installe.

## Meta

Olivier Malenfant-Thuot – malenfantthuotolivier@gmail.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[Github Profile](https://github.com/OMalenfantThuot)
