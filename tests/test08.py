#!/bin/python
bg_to_en_dictionary = {
    "kola":  "car",
    "kuche": "dog",
    "kotka": "cat",
    "kashta": "house"
}

while True:
    print("Admin section")
    user_input = input("")
    if user_input == "":
        break
    bg_word, en_word = user_input.split()
    bg_to_en_dictionary[bg_word] = en_word

while True:
    print("User section")
    user_input = input("")
    if user_input == "":
        break
    if user_input in bg_to_en_dictionary:
        print(bg_to_en_dictionary[user_input])
    else:
        print("Not found")
    

