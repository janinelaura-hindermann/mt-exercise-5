import os
import subprocess
import time


def run_translation_script():
    # Define paths
    scripts = os.path.dirname(os.path.realpath(__file__))
    base = os.path.abspath(os.path.join(scripts, ".."))

    data = os.path.join(base, "scripts", "data")
    configs = os.path.join(base, "configs")
    translations = os.path.join(base, "beam_size_translations")
    config_dir = os.path.join(configs, "bpe_5000_beam_size")

    # Create translations directory if it doesn't exist
    os.makedirs(translations, exist_ok=True)

    # Parameters
    src = "en"
    trg = "de"
    num_threads = 4
    device = 0

    # Measure time
    start_time = time.time()

    # Iterate over all YAML files in the config directory
    for config_file in os.listdir(config_dir):
        if config_file.endswith(".yaml"):
            model_name = os.path.splitext(config_file)[0]
            translations_sub = os.path.join(translations, model_name)
            os.makedirs(translations_sub, exist_ok=True)

            # Define the translation command
            translate_command = [
                "CUDA_VISIBLE_DEVICES={}".format(device),
                "OMP_NUM_THREADS={}".format(num_threads),
                "python3 -m joeynmt translate {} <{} >{}".format(
                    os.path.join(config_dir, config_file),
                    os.path.join(data, f"test.{src}-{trg}.{src}"),
                    os.path.join(translations_sub, f"test.{model_name}.{trg}")
                )
            ]

            # Run the translation command
            translation_output_path = os.path.join(translations_sub, "translation_output.txt")
            with open(translation_output_path, "w") as output_file:
                subprocess.run(" ".join(translate_command), shell=True, stdout=output_file, stderr=subprocess.STDOUT)

            # Compute BLEU score
            bleu_command = [
                "sacrebleu",
                os.path.join(data, f"test.{src}-{trg}.{trg}")
            ]
            bleu_result = subprocess.run(
                bleu_command,
                input=open(os.path.join(translations_sub, f"test.{model_name}.{trg}")).read(),
                text=True,
                capture_output=True
            )

            # Calculate time taken
            elapsed_time = time.time() - start_time

            # Write BLEU score and time taken to the output file
            with open(translation_output_path, "a") as output_file:
                output_file.write("\n" + bleu_result.stdout)
                output_file.write("\ntime taken:\n")
                output_file.write(f"{elapsed_time} seconds\n")

            print(f"Translation completed for {model_name}. Output stored in {translation_output_path}")


if __name__ == "__main__":
    run_translation_script()
