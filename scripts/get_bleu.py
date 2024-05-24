import subprocess
import json


def get_bleu_score(hyp_file, ref_file):
    # Command to compute BLEU score using sacrebleu
    command = f"cat {hyp_file} | sacrebleu --tokenize none {ref_file}"

    # Execute the command and capture the output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Parse the output
    output = result.stdout.strip()

    # Find the JSON line that contains the BLEU score
    try:
        bleu_info = json.loads(output)
        bleu_score = bleu_info.get("score")
        return bleu_score
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


if __name__ == "__main__":
    hyp_file_wordlevel = "../models/model_wordlevel_2/00026000.hyps.test"
    hyp_file_bpe_2000 = "../models/model_bpe_2000/00045000.hyps.test"
    hyp_file_bpe_5000 = "../models/model_bpe_5000/00038500.hyps.test"
    hyp_file_bpe_2000_bpe_data = "../models/model_bpe_2000_bpe_training_data/00045000.hyps.test"
    ref_file = "data/test.en-de.de"

    bleu_score_wordlevel = get_bleu_score(hyp_file_wordlevel, ref_file)
    bleu_score_bpe_2000 = get_bleu_score(hyp_file_bpe_2000, ref_file)
    bleu_score_bpe_5000 = get_bleu_score(hyp_file_bpe_5000, ref_file)

    print(f"BLEU score for word-level: {bleu_score_wordlevel}")
    print(f"BLEU score for BPE 2000: {bleu_score_bpe_2000}")
    print(f"BLEU score for BPE 5000: {bleu_score_bpe_5000}")
