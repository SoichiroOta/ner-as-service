from polyglot.text import Text
from polyglot.downloader import downloader
import spacy


class NERer:
    def __init__(self, library=None, lang=None):
        if library == 'ginza':
            self.nerer = GinzaNERer()
        else:
            self.nerer = PolyglotNERer(lang)

    def recognize(self, blob):
        return self.nerer.recognize(blob)


class PolyglotNERer:
    def __init__(self, lang=None):
        self.lang=lang

    def recognize(self, blob):
        text = Text(blob, hint_language_code=self.lang)
        return [
            {
                'raw': sentence.raw,
                'start': sentence.start,
                'end': sentence.end,
                'entities': [(e.tag, e) for e in sentence.entities],
                'tokens': sentence.tokens,
                'words': sentence.words,
                'language': sentence.language.code
            } for sentence in text.sentences
        ]


class GinzaNERer:
    def __init__(self):
        self.nlp = spacy.load('ja_ginza') 

    def recognize(self, blob):
        doc = self.nlp(blob)
        return doc.to_json()
