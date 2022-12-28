population = [int(el) for el in input().split(', ')]
minimum_wealth = int(input())
output_lst = []
population_length = len(population)
sum_wealth = sum(population)
distribution_not_possible = False
for element in population:
    diff = 0
    if element < minimum_wealth:
        diff = minimum_wealth - element
        element += diff
        output_lst.append(element)
    elif element >= minimum_wealth:
        output_lst.append(element)
    if minimum_wealth * population_length > sum(population):
        distribution_not_possible = True
        break
if distribution_not_possible:
    print("No equal distribution possible")
else:
    if sum(output_lst) > sum_wealth:
        output_lst.pop()
        difference = sum_wealth - sum(output_lst)
        output_lst.append(difference)
        print(output_lst)





