#!/usr/bin/env python3
import argparse
import os


parser = argparse.ArgumentParser(description="Copiar contenido de un archivo a otro.")
parser.add_argument("-i", "--input", type=str, required=True, help="Archivo a copiar.")
parser.add_argument("-o", "--output", type=str, required=True, help="Archivo de destino.")

args = parser.parse_args()

if os.path.isfile(args.input):
    f = open(args.input, "r")
    copia = f.read()
    f.close()
    f2 = open(args.output, "w")
    f2.write(copia)
    f2.close()
else:
    print(f"El archivo {args.input} no existe.")
