

setA = set(['bear', 'cat', 'dog', 'dolphin', 'weasel'])
setB = set(['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion'])
setC = set(['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog'])

sample_space = setA.union(setB).union(setC)


'''
Commutative
A ∪ B = B ∪ A
AB = BA
'''
# print(setA.union(setB) == setB.union(setA))
# print(setA.intersection(setB) == setB.intersection(setA))

a = True
b = False
c = True

# print((a or b) == (b or a))
# print((a and b) == (b and a))



'''
Associative
(A ∪ B) ∪ C = A ∪ (B ∪ C) = A ∪ B ∪ C 
⇒ 5 + (6 + 7) = (5 + 6 ) + 7 = 5 + 6 + 7
(AB)C = A(BC) = ABC
'''
# print((setA.union(setB)).union(setC) == (setC.union(setB)).union(setA))
# print((setA.union(setB)).union(setC) == (setC.union(setB)).union(setA))

a = True
b = False
c = True

# print(((a or b) or c) == (a or (b or c)))


'''
Distributive
A ∪ (BC) = (A ∪ B)(A ∪ C) 
A(B ∪ C) = (AB) ∪ (AC)

5*(2 * 3) = (5 * 2) + (5 * 3)
'''
a = True
b = False
c = True

# print(setA.union(setB.intersection(setC)) == (setA.union(setB)).intersection(setA.union(setC)))

# print((a or (b and c) == (a and b) or (a and c)))



'''
Idempotent Laws
A ∪ A = A
AA = A
'''
a = True
b = False
c = True

# print(setA.union(setA) == setA)
# print((a and a) == a)



'''
Domination Laws
Aside: 
U = Universal Set
The set of which all other subsets are a subset of
∅  = Empty Set = { }
A ∪ U = U
A ∩ U = A
A ∩ ∅ = ∅
'''
a = True
b = False
c = True

# print(setA.intersection(sample_space) == setA)

null_set = set()
print(setA.intersection(null_set) == null_set)