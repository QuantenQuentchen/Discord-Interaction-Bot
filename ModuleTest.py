from Imports import *

Frank = Member("Male", 21, "Frank", False, "No")
Loli = Member("Female", 22, "Loli", False, "No")
Oliver = Member("Male", 11, "Oliver", False, "No")
Steve = Member("Male", 10, "Steve", False, "No")
Frank.add_Offspring(Oliver)
Oliver.add_sibling(Steve)
print(Frank.Offspring[0].Siblings[0])  # .special.stats["Luck"])
# MakeChild(Loli, Frank, False)
print(Frank.Offspring)
print(Oliver.printRelation(False))

# pickle.dump(Frank, open("Frank.p", "wb"))
# Frank = pickle.load(open("Frank.p", "rb"))
# Special().gen_gen(Frank, False)

# Memberlist = pickle.load(open("Test.p", "rb"))
# print(Memberlist[0].Gender)
# print(Memberlist)

# Var = input("Class ? ")

# Var = Member("Male", 12, "Frank", False, "No")
# integrate(Var)

# Special().random_gen()

# for rando in range(100):
#   print(np.random.normal(5,5))
