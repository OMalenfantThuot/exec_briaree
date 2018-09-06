#!/usr/bin/env python3
"""
Script pour renommer les fichiers posinpX.in.ascii
a posinpX.ascii pour les calculs NEB
Peut s'appeler comme un éxécutable
"""

import os

names = os.listdir(os.getcwd())

for name in names:
    if name.endswith(".in.ascii"):
        os.rename(name,name.strip(".in.ascii")+".ascii")
