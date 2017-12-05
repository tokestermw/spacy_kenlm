## spacy_kenlm: KenLM extension for spaCy 2.0

This package adds [kenLM](https://github.com/kpu/kenlm) support
as a [spaCy 2.0 extension](https://spacy.io/usage/processing-pipelines#extensions).

## Usage

Train a `kenLM` language model first (or use the test model from `test.arpa`).

Add the spaCyKenLM to the spaCy pipeline to return scores.

```
import spacy
from spacy_kenlm import spaCyKenLM

nlp = spacy.load('en_core_web_sm')

spacy_kenlm = spaCyKenLM()  # default model from test.arpa

nlp.add_pipe(spacy_kenlm)

doc = nlp('How are you?')

# doc score
doc._.kenlm_score

# span score
doc[:2]._.kenlm_score

# token score
doc[2]._.kenlm_score
```

## Installation

Install from the pip package.

```
pip install spacy_kenlm
```