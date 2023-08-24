import signal
import time

def manejador(signum):
    print("señal {} manejada".format(signum))

signal.signal(signal.SIGUSR1, manejador)

while True:
    time.sleep(1)
    print("Running")
