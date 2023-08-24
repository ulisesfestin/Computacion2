#!/usr/bin/env python3

import os


pid = os.fork()


if pid == 0:
    print(f"I am child {os.getpid()}")
else:
    print(f"I am parent {os.getpid()}")
