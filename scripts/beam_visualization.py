import os
import re
import pandas as pd
import matplotlib.pyplot as plt


def extract_metrics_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract the time taken
    time_taken_match = re.search(r'Generation took ([\d.]+)\[sec\]\.', content)
    time_taken = float(time_taken_match.group(1)) if time_taken_match else None

    # Extract the BLEU score
    bleu_score_match = re.search(r'"score": ([\d.]+),', content)
    bleu_score = float(bleu_score_match.group(1)) if bleu_score_match else None

    return time_taken, bleu_score


def collect_metrics(base_dir):
    data = []
    for subdir in os.listdir(base_dir):
        if subdir.startswith("bpe_5000_beam_"):
            model_name = subdir
            beam_size = int(subdir.split('_')[-1])  # Extract beam size from directory name
            file_path = os.path.join(base_dir, subdir, "translation_output.txt")
            if os.path.exists(file_path):
                time_taken, bleu_score = extract_metrics_from_file(file_path)
                data.append({
                    "Model": model_name,
                    "Beam Size": beam_size,
                    "Time Taken (s)": time_taken,
                    "BLEU Score": bleu_score
                })

    return pd.DataFrame(data)


def visualize_metrics(csv_file_path, output_dir):
    df = pd.read_csv(csv_file_path)

    # Plot Beam Size vs. BLEU Score
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Beam Size'], df['BLEU Score'], marker='o', color='green')
    plt.xlabel('Beam Size')
    plt.ylabel('BLEU Score')
    plt.title('Beam Size vs. BLEU Score')
    plt.grid(True)
    bleu_score_plot = os.path.join(output_dir, 'beam_size_vs_bleu_score.png')
    plt.savefig(bleu_score_plot)
    plt.show()

    # Plot Beam Size vs. Time Taken
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Beam Size'], df['Time Taken (s)'], marker='o', color='orange')
    plt.xlabel('Beam Size')
    plt.ylabel('Time Taken (s)')
    plt.title('Beam Size vs. Time Taken')
    plt.grid(True)
    time_taken_plot = os.path.join(output_dir, 'beam_size_vs_time_taken.png')
    plt.savefig(time_taken_plot)
    plt.show()

    print(f"Plots saved to {output_dir}")


if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../beam_size_translations")
    df = collect_metrics(base_dir)

    # Save to CSV
    output_csv = os.path.join(base_dir, "translation_metrics.csv")
    df.to_csv(output_csv, index=False)
    print(f"Metrics collected and saved to {output_csv}")

    # Visualize metrics
    output_file_path = os.path.join(base_dir)
    visualize_metrics(output_csv, output_file_path)
