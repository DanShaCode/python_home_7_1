
def counter_vowel(frase_list):
    vowel_list = ['а','о','э','е','и','ы','у','ё','ю','я','А','О','Э','Е','И','Ы','У','Ё','Ю','Я']
    vowel_counter = 0
    for frase in frase_list:
        for char in frase:
            for letter in vowel_list:
                if char == letter:
                    vowel_counter += 1       
    return vowel_counter
  