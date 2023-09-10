peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2
if imc < 18.5:
    print(f'Você está abaixo do peso, seu IMC é {imc}!')
elif imc >= 18.5 and imc <= 25.0:
    print(f'Seu peso é o ideal, seu IMC é {imc}!')
elif imc > 25.0 and imc <= 30.0:
    print(f'Você está com sobrepeso, IMC é {imc}')
elif imc > 30.0 and imc <= 40.0:
    print(f'Você tem obesidade, seu IMC é {imc}')
elif imc > 40.0:
    print(f'Você tem obesidade mórbida, seu IMC é {imc}')
