from struct import *
import wave
from nbformat import write


# exercice 1


file = "the_wall.wav"

def exercice1(name):
    f = open(name,"rb")
    data = f.read()
    left = [] ; right = []
    start_data = data.find(b"data") + 8
    # 8 octets = "data" + size of data
    size = unpack_from("I",data,start_data - 4)[0]
    for i in range(size//4):
        # size // 4 =  2696574
        # renvoit un tuple de 2 échantillons chacun codé sur 2 octets
        left.append(unpack_from("hh",data,start_data+i*4)[0])
        right.append(unpack_from("hh",data,start_data+i*4)[1])
    f.close()
    return left,right

# exercice 2, récréer le fichier wav à partir de zéro

"""
pour write si le fichier n'existe pas python le créer
"""
left = exercice1(file)[0] ; right = exercice1(file)[1]

def exercice2(name, left, right):

    with open(name,"wb") as f:
        # en-tête

        f.write(b"RIFF")
        f.write(pack("I",44 + len(left)*4 - 8))
        f.write(b"WAVE")
        f.write(b"fmt")
        f.write(pack("IHHIIHH",16,1,2,44100,176400,4,16))
        f.write(b"data")
        f.write(pack("I",len(left)*4))

        # data

        for i in range(len(left)):
            f.write(pack("hh",left[i],right[i]))

        #print(unpack_from("IIIIIHHIIHHIIhhhh",data,0))

new = "next_wall.wav"


exercice2(new,left,right)

"""
left2 = exercice1(new)[0] ; right2 = exercice1(new)[1]
on a bien left = left2
"""

"""
f = open(new,"rb")
data = f.read()
print(unpack_from("IIIIIHHIIHHIIhh",data,0))

f = open(file,"rb")
data = f.read()
print(unpack_from("IIIIIHHIIHHIIhh",data,0))
"""

"""
Problème : new est différent de file même dans l'en-tête

"""


# exercice 3 : on enlève un échantillon sur deux dans chaque voie

"""
je suppose que la musique va deux fois plus vite
"""


















