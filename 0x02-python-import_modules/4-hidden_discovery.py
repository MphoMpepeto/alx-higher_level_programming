#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    hidden = dir()
    for n in range(0, len(hidden)):
        if hidden[n][:2] != "__":
            print('{:s}'.format(hidden[n]))
