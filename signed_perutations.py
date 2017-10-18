# calculates number of signed permutations


import itertools


def signed_permutation(array):
	return itertools.permutations(array)


permutations = []

N = 4

merged_array = [i + 1 for i in range(N)]
merged_array += [- (i + 1) for i in range(N)]


combinations_of_numbers = itertools.combinations(merged_array, N)

combinations_of_numbers = list(filter(lambda x: len(set(map(abs, x))) == N, combinations_of_numbers))

for sub_array in combinations_of_numbers:
	permutations += signed_permutation(sub_array)

print(len(permutations))
for element in permutations:
	print(' '.join(map(str, element)))
