import re
import streamlit as st
def word_splitter(paragraph : str) -> list[str]:
    words = re.sub("\s+"," ",paragraph) # to check that ultiple spaces are removed coz u know s\+ ...
    return re.split("\s",words)

chukns = []

# def chuker(seprated : list[str],chuk_size: int) -> list[str]:
#     for i in range(0,len(seprated),chuk_size):
#         part = seprated[i:i+chuk_size]
#         chukns.append(part)
    
#     return chukns

# atr = "TThus i sa saloi   as in palaidin ahead injulin oklama juvie"

# emi = word_splitter(atr)
# print(chuker(emi,2))

import requests
#https://weaviate.io/developers/academy/py/standalone/chunking/how_1
def chuker(seperated : list[str], chuk_size : int ,overlap_fraction : float) -> list[str]:
    overlap_int = int(chuk_size * overlap_fraction)
    for i in range(0,len(seperated),chuk_size):
        next = seperated[max(i-overlap_int,0):i+chuk_size]
        # part = " ".join(next)
        # print(part)
        chukns.append(" ".join(next))
    return chukns

url = "https://raw.githubusercontent.com/progit/progit2/main/book/01-introduction/sections/what-is-git.asc"
src_txt = requests.get(url).text

spe = word_splitter(src_txt)
print(chuker(spe,5,0.4))

# repr() - > to  represent a string representation of an object it includes all the special characters toooo.
# we can use pip freeze  > requirements.txt to make a fiel on all the dependencies needed by the project
# after using or cloneing the dir and activating virtual env (requirements.txt) use pip install -r requirements.txt