'''Você é um(a) estudante 🎓 apaixonado(a) por tecnologia que acaba de ser aceito(a) no Vai na Web, uma super escola de tecnologia onde os alunos resolvem desafios de programação para avançar nos estudos.

Mas há um problema! ⚠️ Um vírus misterioso invadiu o sistema, bagunçando notas, permissões de acesso 🔐 e até a segurança da escola. O diretor, Professor Byte, precisa da sua ajuda para restaurar tudo antes que a situação piore!
Resolva os desafios abaixo para recuperar o controle do sistema. Boa sorte, Dev!🚀

(Deve ser feito em Python!)

Instruções do Desafio: 🚨'''

'''Missão 1: Restaurando as Regras Escolares 📝 
O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).'''
nota = 5.99

if nota >=6:
  print(f"O aluno foi aprovado com nota {nota} ")
else:
  print(f"O aluno foi reprovado! Ele precisa de nota igual ou superior a 6 e alcançou apenas {nota}")


'''Missão 2: O Sistema Eleitoral Secreto 📝 
O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).'''
def validate ():
  idade = int(input("Digite a idade do aluno: "))
  if idade < 16:
    print("O usuário ainda não pode votar!")
  else:
    print("O usuário pode votar!")

validate()

'''Missão 3: Recuperando o Sistema de Notas 📊
As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:
- A (90-100) – "Parabéns, você tirou A!"
- B (80-89) – "Muito bem, você tirou B."
- C (70-79) – "Bom trabalho, você tirou C."
- D (60-69) – "Fique atento, você tirou D."
- F (menos de 60) – "Estude um pouco mais, você tirou F.'''

def checkNote ():
  nota = int(input("Digite sua nota (0 a 100): " ))
  if nota < 60 and nota >= 0:
    print("Estude um pouco mais, você tirou F.")
  elif nota >= 60 and nota <70:
    print("Fique atento, você tirou D.")
  elif nota >= 70 and nota < 80:
    print("Bom trabalho, você tirou C.")
  elif nota >=80 and nota < 90:
    print("Muito bem, você tirou B.")
  elif nota >=90 and nota < 100:
    print("Parabéns, você tirou A!")
  else:
    print("Coloque um valor de 0 a 100")  
    checkNote()
checkNote()

'''Missão 4: Restaurando a Identificação de Números ⚖️
Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
Crie um programa que peça dois números ao usuário e exiba a soma deles.'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"A soma de {num1} e {num2} é: ", num1 + num2)


'''Missão 5: Recuperando o Cofre de Segurança 🔒
O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".'''

senha = input("Digite a senha: ")
if senha != "Python123":
  print("Senha incorreta!")
else:
  print("Parabéns! Você acertou a senha!")

'''Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
O vírus está comprometendo o sistema de segurança e a contagem de registros! Para restaurar o funcionamento correto, você precisa reforçar as verificações e garantir que os dados sejam processados corretamente.
  Exiba os números de 1 a 10 usando um loop while. '''

cont = 0
while cont <10:
  print (cont + 1)
  cont +=1
 
'''Missão 7: Organizando a Lista📋
Os números estão misturados e precisam ser organizados! 
Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente!'''

listNumbers = [8,3,10,1,5]
listNumbers.sort()
print("Números em ordem crescente: ", listNumbers)


'''Missão 8: Acessando os Registros de Alunos 🏷️
O sistema de alunos está desordenado! Para acessar as informações corretamente, você precisa organizar os dados.
Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.''' 

tupleStudents = ("Ana", "Bruno","Carla","Daniel", "Eduardo")
print(tupleStudents[0])
print(tupleStudents[-1])

'''Missão 9: Calculando Dobro de um Número 🛠️
Os alunos precisam de um programa que ajude em cálculos rápidos. 
Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
➡️ Exemplo: dobro(5)
➡️   Saída: "O dobro de 5 é 10"'''
def double():
  number = int(input("Digite um número: "))
  print(f"o dobro de {number} é : {number*2 }")
double()

'''Missão 10: Contando Letras 🔄
O sistema precisa contar quantas letras há em um nome.
➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
➡️ Exemplo: contar_letras("Ana")
➡️ Saída:" O nome Ana tem 3 letras"'''

def contLetter():
  name= input("Digite o nome: ")
  print(f"O número de lestras que o nome {name} tem é: {len(name)}")
contLetter()