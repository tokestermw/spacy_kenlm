if __name__ == '__main__':
    import spacy
    from spacy_kenlm import spaCyKenLM

    nlp = spacy.load('en_core_web_sm')

    spacy_kenlm = spaCyKenLM()

    nlp.add_pipe(spacy_kenlm)

    doc = nlp('How are you?')

    assert doc._.kenlm_score < 0

    for token in doc:
        assert token._.kenlm_score < 0

    span = doc[:2]
    assert span._.kenlm_score < 0
