import os
import subprocess


def apply_bpe(input_file, output_file, bpe_code, vocab_file):
    command = f"subword-nmt apply-bpe -c {bpe_code} --vocabulary {vocab_file} --vocabulary-threshold 50 < {input_file} > {output_file}"
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    # Original data files
    data_dir = "data"

    # BPE Output directory
    bpe_dir = "data_sampled"

    # Vocab files generated
    vocab_en = os.path.join("data_sampled/vocab.en")
    vocab_de = os.path.join("data_sampled/vocab.de")

    # Test and dev files
    test_en = os.path.join(data_dir, "test.en-de.en")
    test_de = os.path.join(data_dir, "test.en-de.de")
    dev_en = os.path.join(data_dir, "dev.en-de.en")
    dev_de = os.path.join(data_dir, "dev.en-de.de")

    # BPE encoded output files
    test_bpe_en = os.path.join(data_dir, "test.BPE.en")
    test_bpe_de = os.path.join(data_dir, "test.BPE.de")
    dev_bpe_en = os.path.join(data_dir, "dev.BPE.en")
    dev_bpe_de = os.path.join(data_dir, "dev.BPE.de")

    # BPE code file
    bpe_code = "data_sampled/bpe_code"

    # Apply BPE encoding to test and dev data
    apply_bpe(test_en, test_bpe_en, bpe_code, vocab_en)
    apply_bpe(test_de, test_bpe_de, bpe_code, vocab_de)
    apply_bpe(dev_en, dev_bpe_en, bpe_code, vocab_en)
    apply_bpe(dev_de, dev_bpe_de, bpe_code, vocab_de)
