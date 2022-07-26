import random

print("Добро пожаловать в генератор 8ми значных паролей.")

def godnui_parol():
    s1 = "ABCDFEGHIJKLMNOPQRSTUWXYZ"
    s2 = "abcdefghijklmnopqrstuwxyz"
    s3 = "0123456789"
    dlina = 8
    generate = s1 + s2 + s3
    password = "".join(random.sample(generate,dlina))
    print(password)

godnui_parol()


