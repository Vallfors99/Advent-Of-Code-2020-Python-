import sys
input_file = sys.stdin


def getUniqueAlgs(algs):  # get all unique allergens from set of sets of allergens
    list_algs = [a for A in algs for a in A]
    uniqueAlgs = set(list_algs)
    return uniqueAlgs


def findAlgInSets(algs, algSets):
    potential_dict = dict()
    for alg in algs:
        for idx in range(0, len(algSets)):
            if alg in algSets[idx]:
                if alg in potential_dict:
                    potential_dict[alg].append(idx)
                else:
                    potential_dict[alg] = [idx]
    return potential_dict


def findAlgInFood(pot_algs, foodSets):
    algCouldBe = dict()
    for alg in pot_algs:
        for foodID in pot_algs[alg]:
            if alg in algCouldBe:
                algCouldBe[alg] = algCouldBe[alg].intersection(
                    foodSets[foodID])
            else:
                algCouldBe[alg] = foodSets[foodID]
    return algCouldBe


def solveDictionary(Dict_in):  # solve set of matching ingredients and allergens
    totalSolved = 0
    AlreadyRemoved = []
    while totalSolved < len(Dict_in)-1:
        for key in Dict_in:
            if len(Dict_in[key]) == 1 and Dict_in[key] not in AlreadyRemoved:
                removeWord = next(iter(Dict_in[key]))
                totalSolved += 1
                AlreadyRemoved.append(removeWord)
                for otherKey in Dict_in:
                    if otherKey != key:
                        Dict_in[otherKey] = [
                            elem for elem in Dict_in[otherKey] if elem != removeWord]
    return Dict_in


input_file = open(sys.argv[1], 'r')
# input prep..
lines = input_file.readlines()
lines = [line.rstrip(")\n").replace("contains", " ").split(
    "(") for line in lines]

foods_sets = [line[0].split(" ") for line in lines]
foods_sets = [set([subfood for subfood in food if subfood != ""])
              for food in foods_sets]
allergen_sets = [set(line[1].split(",")) for line in lines]
allergen_sets = [set([suball.replace(" ", "") for suball in aller])
                 for aller in allergen_sets]

# solution
unique_allergens = getUniqueAlgs(allergen_sets)
potentialAlg = findAlgInSets(unique_allergens, allergen_sets)
possibleMatchDict = findAlgInFood(potentialAlg, foods_sets)
# We have a dictionary of allergens and ings potentially containing them. Lets solve it!
allergens_solved = solveDictionary(possibleMatchDict)

# now we create a set with all allergens and remove ings containing allergens
finalAllergens = (list(allergens_solved.values()))
finalAllergens = set([elem for sublist in finalAllergens for elem in sublist])
Safe_per_food = []
for subset in foods_sets:
    subset = subset.difference(finalAllergens)
    Safe_per_food.append(subset)

Safe_total = sum([len(safe_row) for safe_row in Safe_per_food])
print(f'total occurences of safe ingredients: {Safe_total}')

# part-2
res = ""
sorted_keys = sorted(allergens_solved)
for key in sorted_keys:
    res = res + str(allergens_solved[key][0]) + ","
res = res[:-2]
print(f'dangerous ingredients in ordered alphabetically by allergen: \n {res}')
input_file.close()
