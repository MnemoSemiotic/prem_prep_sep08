

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

print(((a or b) or c) == (a or (b or c)))


'''
Distributive
A ∪ (BC) = (A ∪ B)(A ∪ C) 
A(B ∪ C) = (AB) ∪ (AC)
'''

