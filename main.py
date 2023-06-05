message = "abcde"

def split_message(mess):
    text_split = list(mess)
    return text_split

def chiffre_message(mess, cle = 2):
    temp = []
    for i in range(len(mess)):
        temp.append(chr(ord(mess[i]) + cle))
        resultat = "".join(temp)
    return resultat

def reconstitution_message(mess, cle = 2):
    mess_dechiffrer = []
    for i in range(len(mess)):
        mess_dechiffrer.append(chr(ord(mess[i]) - cle))
        resultat = "".join(mess_dechiffrer)
    print(resultat)
        


message_en_caractere = split_message(message)
chiffrer = chiffre_message(message_en_caractere)



# chiffrer = chiffre_message(message_en_caractere, -2)
# print(chiffrer)

dechiffrer = reconstitution_message(chiffrer)
    