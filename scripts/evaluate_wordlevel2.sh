#! /bin/bash

scripts=$(dirname "$0")
# base = parent of the scripts directory
base=$scripts/..

data=$base/scripts/data
configs=$base/configs

translations=$base/translations

# make new directory
mkdir -p $translations

# source and target language
src=en
trg=de

num_threads=4
device=0

# measure time

SECONDS=0

model_name=wordlevel_2

echo "###############################################################################"
echo "model_name $model_name"

translations_sub=$translations/$model_name

mkdir -p $translations_sub

CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python3 -m joeynmt translate $configs/$model_name.yaml <$data/test.$src-$trg.$src >$translations_sub/test.$model_name.$trg

# compute case-sensitive BLEU

cat $translations_sub/test.$model_name.$trg | sacrebleu $data/test.$src-$trg.$trg

echo "time taken:"
echo "$SECONDS seconds"
