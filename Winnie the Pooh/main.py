import os
from modules.vow_counter import *
from modules.checker import *

os.system('cs||clear')

print()
frase_list = input("Введите, пожалуйста, фразу: ").split(' ')
song_rythm = list(map(counter_vowel, frase_list))

print()
check_song_rythm(song_rythm)

print()
user_await = input("Нажмите Enter")
os.system('cs||clear')