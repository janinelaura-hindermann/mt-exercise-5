import os
import subprocess


def run_subword_nmt_learn_bpe(train_file_en, train_file_de, num_operations, codes_file, vocab_file_en, vocab_file_de):
    command = (
        f"subword-nmt learn-joint-bpe-and-vocab --input {train_file_en} {train_file_de} "
        f"-s {num_operations} -o {codes_file} --write-vocabulary {vocab_file_en} {vocab_file_de} --total-symbols"
    )
    print(f"Running command: {command}")
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    # Base directory
    base_dir = os.path.abspath(os.path.dirname(__file__))

    # Directories
    data_dir = os.path.join(base_dir, "data_sampled")
    output_dir = os.path.join(base_dir, "data_bpe_5000")
    os.makedirs(output_dir, exist_ok=True)

    # Training files
    train_file_en = os.path.join(data_dir, "sampled_train.en-de.en")
    train_file_de = os.path.join(data_dir, "sampled_train.en-de.de")

    # BPE files
    codes_file = os.path.join(output_dir, "bpe_code_5000.bpe")
    vocab_file_en = os.path.join(output_dir, "vocab.en")
    vocab_file_de = os.path.join(output_dir, "vocab.de")

    # Number of BPE operations
    num_operations = 5000

    # Run BPE learning
    run_subword_nmt_learn_bpe(train_file_en, train_file_de, num_operations, codes_file, vocab_file_en, vocab_file_de)
