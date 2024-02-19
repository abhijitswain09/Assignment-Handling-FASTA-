#import all the necessary packages
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from random import choice

# Function to reverse complement a sequence
def reverse_complement(sequence):
    return str(Seq(sequence).reverse_complement())

# Function to introduce a random 1 nucleotide change
def introduce_random_change(sequence):
    if len(sequence) > 0:
        position = choice(range(len(sequence)))
        new_base = choice('ACTG'.replace(sequence[position], ''))
        mutated_sequence = sequence[:position] + new_base + sequence[position + 1:]
        return mutated_sequence
    else:
        return sequence

# Function to process a subsequence and insert it back into the primary sequence
def process_and_insert(primary_sequence, start, end):
    subsequence = str(primary_sequence[start-1:end])  # 0-based indexing in Python
    reversed_complement = reverse_complement(subsequence)
    processed_subsequence = introduce_random_change(reversed_complement)
    
    primary_sequence = primary_sequence[:start-1] + processed_subsequence + primary_sequence[end:]
    return primary_sequence

# Your influenza genome file
genome_filename = "influenza.fna"

# Read the primary multi-fasta file using SeqIO.parse
genome_records = SeqIO.parse(genome_filename, "fasta")

# Create a BED file with coordinates for at least 3 locations
bed_content = """\
Scaffold1\t100\t200
Scaffold2\t300\t400
Scaffold3\t500\t600
"""

bed_filename = "influenza.bed"

# Save the BED content to a file
with open(bed_filename, "w") as bed_file:
    bed_file.write(bed_content)

# Read the BED file and process/insert sequences into the primary sequence
for record in genome_records:
    genome = record  # Assuming you want to process each sequence in the file
    with open(bed_filename, "r") as bed_file:
        for line in bed_file:
            scaffold, start, end = line.strip().split("\t")
            start, end = int(start), int(end)
            genome.seq = process_and_insert(genome.seq, start, end)

    # Save the modified sequence to an output file
    output_filename = "output_influenza.fasta"
    output_record = SeqRecord(genome.seq, id=genome.id, description=genome.description)
    SeqIO.write([output_record], output_filename, "fasta")

    print(f"Processed influenza genome saved to {output_filename}")

