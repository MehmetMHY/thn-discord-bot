import subprocess
import time
import sys
import os

# [global] bool for logging and/or print messages
show = False

# log/print messages (if enabled)
def log_print(msg, tshow=False):
    global show
    message = "[DAUDIO] " + str(msg)
    if show or tshow:
        print(message)

# save terminal command output
def term_output(cmd):
    proc = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE,)
    output = proc.communicate()[0].decode("utf-8")
    lines = output.split("\n")
    return lines


x = term_output("cat google_words.txt")


for i in x:
    print(i[0:i.find("|")])

