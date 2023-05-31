#!/usr/bin/env python3
import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Inversor de texto')
parser.add_argument('-f', '--file', help='Archivo a utilizar', required=True)
args = parser.parse_args()

pipes = []

with open('texto.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        r, w = os.pipe()
        pid = os.fork()
        if pid == 0:
            os.close(r)
            reversed_line = line.strip()[::-1]
            os.write(w, reversed_line.encode())
            os.close(w)
            # print("Proceso padre terminado")
            sys.exit(0)
        else:
            os.close(w)
            pipes.append((pid, r))
            # print("Proceso hijo terminado")

inverted_lines = []
# print(pipes)

for pid, r in pipes:
    os.waitpid(pid, 0)
    inverted_line = os.read(r, 100).decode()
    inverted_lines.append(inverted_line)

for line in inverted_lines:
    print(line)
