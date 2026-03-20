import data
import sys
import time
import random


# Text typer function
def print_slow(str):
    for char in str:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
