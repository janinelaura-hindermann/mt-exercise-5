import os
import subprocess


def apply_bpe(input_file, output_file, bpe_code, vocab_file):
    command = f"subword-nmt apply-bpe -c {bpe_code} --vocabulary {vocab_file} --vocabulary-threshold 50 < {input_file} > {output_file}"
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    # Original data files
    data_dir = "data"

    # BPE Output directory
    bpe_dir = "data_bpe"
    os.makedirs(bpe_dir, exist_ok=True)

    # Vocab files generated
    vocab_en = os.path.join(bpe_dir, "vocab.en")
    vocab_de = os.path.join(bpe_dir, "vocab.de")

    # Test and dev files
    test_en = os.path.join(data_dir, "test.en-de.en")
    test_de = os.path.join(data_dir, "test.en-de.de")
    dev_en = os.path.join(data_dir, "dev.en-de.en")
    dev_de = os.path.join(data_dir, "dev.en-de.de")

    # BPE encoded output files
    test_bpe_en = os.path.join(bpe_dir, "test.en-de.en")
    test_bpe_de = os.path.join(bpe_dir, "test.en-de.de")
    dev_bpe_en = os.path.join(bpe_dir, "dev.en-de.en")
    dev_bpe_de = os.path.join(bpe_dir, "dev.en-de.de")

    # BPE code file
    bpe_code = os.path.join(bpe_dir, "bpe_code")

    # Apply BPE encoding to test and dev data
    apply_bpe(test_en, test_bpe_en, bpe_code, vocab_en)
    apply_bpe(test_de, test_bpe_de, bpe_code, vocab_de)
    apply_bpe(dev_en, dev_bpe_en, bpe_code, vocab_en)
    apply_bpe(dev_de, dev_bpe_de, bpe_code, vocab_de)

    print(f"BPE encoded test files: {test_bpe_en}, {test_bpe_de}")
    print(f"BPE encoded dev files: {dev_bpe_en}, {dev_bpe_de}")
