import os

# File paths
src_file_de = 'data/train.en-de.de'
src_file_en = 'data/train.en-de.en'

# Output directory
output_dir = 'data_sampled'
os.makedirs(output_dir, exist_ok=True)

# Output file paths
output_file_de = os.path.join(output_dir, 'sampled_train.en-de.de')
output_file_en = os.path.join(output_dir, 'sampled_train.en-de.en')

# Number of lines to sample
num_lines_to_sample = 100000


def sample_lines(input_file, output_file, num_lines):
    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile):
            if i < num_lines:
                outfile.write(line)
            else:
                break


# Sample the lines from each file
sample_lines(src_file_de, output_file_de, num_lines_to_sample)
sample_lines(src_file_en, output_file_en, num_lines_to_sample)

print(f"Sampled {num_lines_to_sample} lines and saved to {output_dir}.")


# Sanity check to ensure both files have the same number of lines
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)


num_lines_de = count_lines(output_file_de)
num_lines_en = count_lines(output_file_en)

if num_lines_de == num_lines_en:
    print(f"Sanity check passed: Both files contain the same number of lines ({num_lines_de} lines).")
else:
    print(f"Sanity check failed: Files contain different number of lines (DE: {num_lines_de}, EN: {num_lines_en}).")
