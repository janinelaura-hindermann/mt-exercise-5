# MT Exercise 5: Byte Pair Encoding, Beam Search

This repository is a starting point for the 5th and final exercise. As before, fork this repo to your own account and
the clone it into your prefered directory.

## Requirements

- This only works on a Unix-like system, with bash available.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

  `pip install virtualenv`

## Steps

Clone your fork of this repository in the desired place:

    git clone https://github.com/[your-name]/mt-exercise-5

Create a new virtualenv that uses Python 3.10. Please make sure to run this command outside of any virtual Python
environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software as described in the exercise pdf.

Download data:

    ./download_iwslt_2017_data.sh

Before executing any further steps, you need to make the modifications described in the exercise pdf.

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Evaluate a trained model with

    ./scripts/evaluate.sh

---

# Modifications

Languages:

- English (src)
- German (trg)

So we take data with "en-de".

## Sample Training Data

As mentioned in the exercise description, we should sub-sample the training data to 100k sentence pairs.
For doing this, we created a script in the `scripts`directory.

    sub_sample_training_data.py

This script takes the training data provided in the `data` directory and creates a sub-sampled version of it with 100k
sentence pairs and stores it in the `data_sampled` directory. It also provides a little sanity check if both files
contain the same number of lines. If you want to execute this script with your own data, please change the original data
source path in the script directly.

## Config Files

We added config files for the word-level and the bpe model in the `configs` directory.

    bpe_config.yaml
    wordlevel_config.yaml

