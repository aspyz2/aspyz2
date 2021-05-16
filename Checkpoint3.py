'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Check Point 3
Alunos
Enzo Aparecido Viana RM 88883
'''
from sklearn import tree
# features = 10 referencias de cada
features = [99, 120, 60], [80, 139, 100], [94, 60, 98], [60, 30, 80], [76, 90, 120], [94, 112, 70], [83, 121, 32], [89, 78, 135], [22, 123, 97], [54, 93, 128], [101, 141, 189], [124, 146, 104], [124, 159, 198], [120, 148, 180], [121, 186, 120], [
    112, 196, 160], [115, 154, 100], [107, 167, 198], [109, 187, 180], [123, 199, 120], [126, 241, 289], [127, 200, 204], [129, 259, 298], [130, 248, 280], [131, 286, 220], [142, 296, 260], [165, 254, 200], [167, 267, 298], [199, 287, 280], [143, 299, 220]
# 0 = glicemia normal , 1 = tolerancia e 2 = diabetes
labels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
          1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
gli = int(input('Digite sua glicemia em jejum :  '))
tol = int(input("Digite sua glicemia em Pós-Sobrecarga :  "))
diab = int(input("Digite sua glicemia casualmente :  "))
x = classif.predict([[gli, tol, diab]])
if x == 0:
    print('Sua glicose está normal! :) ')
elif x == 1:
    print('Você tem baixa tolerancia a glicose :(')
else:
    print('Você tem diabetes ;( ')
print("As resposta dadas pelo programa devem ser analizadas por um médico especialista e não devem ser usadas como verdade absoluta.")
