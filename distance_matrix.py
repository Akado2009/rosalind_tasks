from Bio import SeqIO

def parse_fasta(fasta):
	array = [] 
	with open(fasta, "rU") as handle:
		for record in SeqIO.parse(handle, "fasta"):
			array.append(record.seq)

	return array

def calculate_distance_matrix(sequences):
	distance_matrix = [[0 for i in range(len(sequences))] for i in range(len(sequences))]
	for i in range(len(sequences)):
		for j in range(len(sequences)):
			distance_matrix[i][j] = calculate_distance(sequences[i], sequences[j])
	return distance_matrix


def calculate_distance(seq_1, seq_2):
	return float(sum([1 for i in range(len(seq_1)) if seq_1[i] != seq_2[i]]))/len(seq_1)

def main(fasta):
	contents = parse_fasta(fasta)
	matrix = calculate_distance_matrix(contents)
	for row in matrix:
		print(' '.join(map(str, row)))


if __name__ == '__main__':
	main('q.fasta')
