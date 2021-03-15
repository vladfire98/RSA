# -*- coding: utf-8 -
import random
import struct
from tkinter import *

def minverse(x,y):
    for i in range(0,y):
        if (x*i)%y == 1:
            return i

# Шифрует сообщение, используя RSA
def encrypt(m,n,e):
    r = 1
    while e:
        if e & 1:
            r = (r * m) % n
        m *= m
        m %= n
        e >>= 1
    return r

# Расшифровывает сообщение, зашифрованное в RSA
def decrypt(c, d ,n):
    r = 1
    while d:
        if d & 1:
            r = (r * c) % n
        c *= c
        c %= n
        d >>= 1
    return r

p = 23
q = 29
n = p * q
phi = (p-1)*(q-1)

e = 241

d = minverse(e,phi)
pub = str(n) + str(e)

def shifr(file):
    filename1 = file
    filename2 = "en" + filename1
    file1 = open(filename1, mode = 'br')
    file2 = open(filename2, mode = 'bw')
    size=4
    par = file1.read(size)
    while par != b'':
        print(par)
        par=encrypt(struct.unpack("i", par)[0],e,n)
        print(file2.write(struct.pack("i", par)))
        par=file1.read(size)

def rashifr(file):
    filename11 = file
    filename12 = "d" + filename11
    file3 = open(filename11, mode='br')
    file4 = open(filename12, mode='bw')

    size1=4
    par1 = file3.read(size1)
    while par1 != b'':
        print(par1)
        par1 = decrypt(struct.unpack("i", par1)[0],d,n)
        print(file4.write(struct.pack("i", par1)))
        par1=file3.read(size1)

def goshifr():    
    shifr(file.get())
    e = int(key.get())
    d = minverse(e,phi)
    print("Public Key:")
    print("n = " + str(n))
    print("e = " + str(e))
    pub = str(n) + str(e)
    print("Private Key:")
    print("d = " + str(d))


def gorashifr():    
    rashifr(file.get())
    e = int(key.get())
    d = minverse(e,phi)
    print("Public Key:")
    print("n = " + str(n))
    print("e = " + str(e))
    pub = str(n) + str(e)
    print("Private Key:")
    print("d = " + str(d))

    

root = Tk()
root.geometry('300x100')
root.title("RSA Crypert/Decrypter")
 
file = StringVar()
key = StringVar()
 
file_label = Label(text="file: ")
key_label = Label(text="key: ")
 
file_label.grid(row=0, column=0)
key_label.grid(row=1, column=0)
 
file_entry = Entry(textvariable=file)
key_entry = Entry(textvariable=key)
 
file_entry.grid(row=0,column=1, padx=5, pady=5)
key_entry.grid(row=1, column=1, padx=5, pady=5)
 


enc_button = Button(text="enc", command=goshifr)
enc_button.grid(row=2, column=0, padx=5, pady=5)

dec_button = Button(text="dec", command=gorashifr)
dec_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()