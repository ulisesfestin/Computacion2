#!/usr/bin/env python3
import argparse
import datetime
import os
import subprocess

parser = argparse.ArgumentParser(description='Ejecuta un comando y guarda su salida y log')
parser.add_argument('-c', '--command', type=str, required=True,
                    help='comando a ejecutar')
parser.add_argument('-f', '--output_file', type=str, required=True,
                    help='archivo donde se guarda la salida del comando')
parser.add_argument('-l', '--log_file', type=str, required=True,
                    help='archivo donde se guarda el registro del comando')
args = parser.parse_args()

if not os.path.exists(args.output_file):
    open(args.output_file, 'w').close()

if not os.path.exists(args.log_file):
    open(args.log_file, 'w').close()

process = subprocess.Popen(args.command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
with open(args.output_file, 'a') as f:
    f.write(stdout.decode())

if stderr:
    log_message = f"{datetime.datetime.now()}: {args.command}: {stderr.decode()}"
else:
    log_message = f"{datetime.datetime.now()}: Comando \"{args.command}\" ejecutado correctamente.\n"
with open(args.log_file, 'a') as f:
    f.write(log_message)
