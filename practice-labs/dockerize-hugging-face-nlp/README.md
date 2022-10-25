<link rel='stylesheet' href='../../assets/css/main.css'/>

## Lab: Dockerize an NLP Program !

## Overview

NLP (Natural Language Processing) has really advanced in the last few years.  Advances in deep learning research is pushing the boundaries.

One of the popular deep learning models for NLP is  [Hugging Face's Transformer library](https://github.com/huggingface/transformers)

Here is the [documentation](https://huggingface.co/transformers/usage.html)

## Step-1: Try the online demo!

[Allen NLP Transformer QA](https://demo.allennlp.org/reading-comprehension/transformer-qa)

Give it some 'reading materials' and ask questions!

## Step-2: Dockerize the NLP API

In this step, we will write a python code to use the NLP API.

And we will dockerize this code

Look at the python code [qa-hf.py](qa-hf.py)

Make a note of the dependencies it needs

## Step-3: Dockerfile

Inspect and update [Dockerfile](Dockerfile)

## Step-4: Build the image

```bash
$   docker build . -t hf-nlp
```

## Step-5: Test The Image

```bash
$   docker run -it hf-nlp
```

Run this inside the container

```bash
# inside the container
$   python qa-hf.py
# observe the results
```

## Step-6: Improve the container

you will notice, when you run the `python qa-hf.py`  for the first time, it needs to download the NLP model.

But it is not saved in the container.  Every time you start the container, it needs to re-download the model.

Can you fix this?  How will you approach this?