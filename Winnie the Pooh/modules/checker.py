
def check_song_rythm(song_rythm):
    flag = 0
    for index in range(len(song_rythm) - 1):
        if song_rythm[index] == song_rythm[index + 1]:
            continue
        else:
            flag += 1
            break
    if flag == 0:
        awnser = print("Парам пам-пам")
        return awnser
    if flag == 1:
        awnser = print("Пам парам")
        return awnser