#!/usr/bin/env python

import fire
from nlplogic.corenlp import summarize_wikipedia, get_phrases


def main(name, length=1):
    text = summarize_wikipedia(name, length)
    phrases = get_phrases(text)
    return phrases


if __name__ == "__main__":
    fire.Fire(main)
