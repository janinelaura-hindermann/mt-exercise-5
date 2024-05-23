import os


def remove_counts(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            token = line.split()[0]
            outfile.write(f"{token}\n")


def concatenate_vocab_files(vocab_en, vocab_de, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        with open(vocab_en, 'r', encoding='utf-8') as infile_en:
            outfile.write(infile_en.read())
        with open(vocab_de, 'r', encoding='utf-8') as infile_de:
            outfile.write(infile_de.read())


def sort_and_remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    unique_lines = sorted(set(lines))
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(unique_lines)


def delete_intermediate_files(*files):
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print(f"Error: {file} : {e.strerror}")


if __name__ == "__main__":
    # Directories
    base_dir = os.path.abspath(os.path.dirname(__file__))
    data_bpe_dir = os.path.join(base_dir, "data_bpe")

    # Ensure the data_bpe directory exists
    os.makedirs(data_bpe_dir, exist_ok=True)

    # Files generated
    vocab_en = os.path.join(data_bpe_dir, "vocab.en")
    vocab_de = os.path.join(data_bpe_dir, "vocab.de")

    # Output files
    vocab_en_clean = os.path.join(data_bpe_dir, "vocab_clean.en")
    vocab_de_clean = os.path.join(data_bpe_dir, "vocab_clean.de")
    joint_vocab_raw = os.path.join(data_bpe_dir, "joint_vocab_raw.txt")
    joint_vocab_sorted = os.path.join(data_bpe_dir, "joint_vocab_sorted.txt")
    joint_vocab_clean = os.path.join(data_bpe_dir, "joint_vocab_clean.txt")

    # Step 1: Remove counts from individual vocab files
    remove_counts(vocab_en, vocab_en_clean)
    remove_counts(vocab_de, vocab_de_clean)

    # Step 2: Concatenate cleaned vocab files
    concatenate_vocab_files(vocab_en_clean, vocab_de_clean, joint_vocab_raw)

    # Step 3: Sort and remove duplicates from the concatenated file
    sort_and_remove_duplicates(joint_vocab_raw, joint_vocab_clean)

    # Delete intermediate files
    delete_intermediate_files(vocab_en_clean, vocab_de_clean, joint_vocab_raw, joint_vocab_sorted)

    # Print the final output file name
    print(f"Clean joint vocabulary created: {joint_vocab_clean}")
