from __future__ import unicode_literals

import os

import kenlm

from spacy.tokens import Doc, Span, Token

from spacy_kenlm._about import __version__

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TEST_PATH = os.path.join(ROOT_DIR, 'test.arpa')


def default_tokenizer(doc):
    return [token.text for token in doc]


class spaCyKenLM(object):

    name = 'kenlm'

    def __init__(self, path=TEST_PATH, tokenizer=None):

        self.path = path
        self.kenlm = kenlm.Model(self.path)
        if tokenizer is None:
            self.tokenizer = default_tokenizer

        Doc.set_extension('kenlm_score', getter=self.get_span_score)
        Span.set_extension('kenlm_score', getter=self.get_span_score)
        Token.set_extension('kenlm_score', default=0.)
        # TODO: add perplexity?

        Doc.set_extension('kenlm_full_scores', getter=self.get_full_scores)

    def __call__(self, doc):

        full_scores = doc._.kenlm_full_scores
        
        for token, score in zip(doc, full_scores):
            token._.kenlm_score = score
        
        return doc

    def get_full_scores(self, doc):
        tokens = self.tokenizer(doc)
        text = ' '.join(tokens)
        full_scores = self.kenlm.full_scores(text, bos=True, eos=True)
        return [score for score, ngram_size, is_oov in full_scores]

    def get_span_score(self, span):
        score = 0.
        for token in span:
            score += token._.kenlm_score
        return score
