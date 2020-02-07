#!/usr/bin/python3

import r2pipe
import time
import os

r = r2pipe.open("fib2")

r.cmd("aa;ood;dcu main")
os.system("clear")

def printRegs():
    rax = r.cmd("dr~rax | grep -v orax").split(" ")[2].strip()
    rbx = r.cmd("dr~rbx").split(" ")[2].strip()
    rcx = r.cmd("dr~rcx").split(" ")[2].strip()
    rdx = r.cmd("dr~rdx").split(" ")[2].strip()
    rdi = r.cmd("dr~rdi").split(" ")[2].strip()
    rsi = r.cmd("dr~rsi").split(" ")[2].strip()
    print("\nrax: " + rax + "\trbx:" + rbx + "\trcx: " + rcx + "\nrdx: " + rdx + "\trdi: " + rdi + "\trsi:" + rsi)
    print("\n\n")
    print(r.cmd("pxa@rsp"))

while True:
    r.cmd("ds")
    os.system("clear")
    print(r.cmd("pd 10"))
    print("\n\n")
    printRegs()
    input()
