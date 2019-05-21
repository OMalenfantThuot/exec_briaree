# Exec\_briaree
> Fichier contenant des executables a utiliser sur Briaree

<p align="center">
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

Les executables sont dans le fichier bin/.

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

[Github Profile](https://github.com/OMalenfantThuot)
