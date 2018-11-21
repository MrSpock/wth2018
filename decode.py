#!/usr/bin/env python3
def decode(data):
    # convert 36 bits to long integer
    value=int(data,2)
    # remove 12 least significant bits by shifting >> 12
    value=value >> 12
    # remove preambule - only 12 least significant bits are important
    value=value & 0xfff
    # lets check do we have negative temperature by comparing bits 10-12
    # 0xf00 is 111100000000. We are checking value of 3 most significant bits
    # if set to 111 - negative temp. If set 000 - positive
    if (value & 0xe00) == 0xe00:
        # Negative algorythm
        return ((value & 0xff) - 256) / 10.0
    else:
        # Positive temp algorythm
        return (value & 0x1ff)/10.0

DATA="101001101000111101110011111100000000"
VALUE=-14.1
if VALUE == decode(DATA):
    print("Algorytm poprawny:\n{} ->{}".format(DATA, VALUE))
else:
    print("Próbuj dalej ..")

