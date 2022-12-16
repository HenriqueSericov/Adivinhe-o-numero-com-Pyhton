import random

print("Seja muito bem vindo! Será que consegue adivinhar o numero?")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é numerico. Favor execute novamente e informe um numero! ")
    quit()

ramdom_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Adivinhe o numero: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é numerico. Favor execute novamente e informe um numero! ")
        continue
    n_choices = n_choices + 1
    if answer_user == ramdom_number:
        print("Acertou!")
        break
    elif answer_user > ramdom_number:
        print("Muito alto! O numero é menor doque isso!")
    else:
        print("Muito baixo! O numero é maior doque isso")

print("Numero de tentativas : " +str(n_choices))