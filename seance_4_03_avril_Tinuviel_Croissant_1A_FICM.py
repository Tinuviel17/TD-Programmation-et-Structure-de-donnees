import matplotlib.pyplot as plt

## class Hashtable
# self est un tableau dont les cases sont des listes

def hash_naive(chain, length):
    return (sum([ord(c) for c in chain]))%length

def hash_complex(chain, length):
    h = 0
    for c in chain:
        h = 33*h + ord(c)
    return h%length

class Hashtable:
    def __init__(self, f, length = 4):
        self._function = f
        self._len = length
        self._table = [[] for i in range(length)]

    def put(self,key,value):
        index = self._function(key,self._len)
        nb_element = 0
        for i in range(self._len):
            nb_element += len(self._table[i])

        if self._table[index] == [] :
            """la case de cet index est vide, on peut lui assigner un couple (key,value)"""
            self._table[index].append((key,value))

        if key in [self._table[index][i][0] for i in range (len(self._table[index]))]:
            """cette clé existe déjà dans l'index, on fait donc une mise à jour du tuple (key,value)"""
            for i in range(len(self._table[index])):
                if self._table[index][i][0] == key:
                    self._table[index][i] = (key,value)

        if nb_element + 1 > 1.2*self._len :
            """si on dépasse un certain nombre d'éléments, on agrandit la table"""
            tableau = self._table
            self._len = 2 * self._len
            self._table = [[] for i in range(self._len)]
            for j in range(len(tableau)):
                self._table[j] = tableau[j]

        if key not in [self._table[index][i][0] for i in range (len(self._table[index]))]:
            """cet index ne contient pas encore de couple (key,value) avec cette valeur de clé, on peut donc lui assigner le couple (key,value) """
            self._table[index].append((key,value))
        return self


    def get(self,key):
        """renvoie valeur associée à la clé"""
        index = self._function(key,self._len)
        for i in range (len(self._table[index])):
            if key == self._table[index][i][0]:
                return self._table[index][i][1]
        return None

    def repartition(self):
        N = self._len
        x = range(N)
        """x représente les index du tableau"""
        y=[]
        for index in range(N):
            y.append(len(self._table[index]))
            """ on reagarde ke nombre de collisions dans chaque case du tableau"""
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

    def __str__(self):
        return f" Table : {self._table}"


def ex5():
    liste = []
    f = open("frenchssaccent.dic",'r')
    for ligne in f:
        liste.append(ligne[0:len(ligne)-1])
        """liste de mot complète sans retours à la ligne"""
    f.close()
    table = Hashtable(hash_naive,320)
    for mot in liste :
        table.put(mot,len(mot))
    return table._table

# exercice 2
t1 = Hashtable(hash_complex)
#print(t1)
#hash_naive('abc',3)
t2 = t1.put('abc',3)
t3 = t2.put('abc',4)
#print(t2)

# exercice 3
#print(t2.get('abc'))
#print(t2.get('aaa'))

# exercice 4
t4 = t1.put('abc',5).put('aa',5).put('g',3)
#print(t4)
#t4.repartition()

# exercice 5
# ex5()


# exercice 6
table = Hashtable(hash_complex)
t1 = table.put('abc',5).put('a',5).put('g',3).put('bb',4)
#print(t1)
t2 = t1.put('aa',8).put('z',3).put('bi',7).put('gze',2)
#print(t2)
t3 = t2.put('gvze',7)
#print(t3)






