#!/usr/bin/env python3
import argparse
import os
import sys

def calculate_sum_pares(pid):
    start_message = f"Ejecutando proceso hijo {pid}..."
    end_message = f"Terminado el proceso hijo {pid}!"
    if args.verbose:
        print(start_message)
    suma_pares = 0
    for i in range(pid):
        if i % 2 == 0:
            suma_pares += i
    if args.verbose:
        print(end_message)
    print(f"{pid} - {os.getppid()} : {suma_pares}")


parser = argparse.ArgumentParser(description='Suma de pares desde 0 hasta el PID')
parser.add_argument('-n', dest='num_procs', type=int, help='numero de procesos hijos a crear', required=True)
parser.add_argument('-v', dest='verbose', action='store_true', help='habilitar modo verboso')
args = parser.parse_args()

for i in range(args.num_procs):
    pid = os.fork()
    if pid == 0:
        calculate_sum_pares(os.getpid())
        sys.exit()

for i in range(args.num_procs):
    os.wait()
