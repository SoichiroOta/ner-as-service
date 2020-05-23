import os

from polyglot.downloader import downloader


env = os.environ
LANG = env.get('LANG')


def download(lang=None):
    if lang is None:
        language = 'en'
    else:
        language = lang

    downloader.download("embeddings2." + language)
    supported_tasks = downloader.supported_tasks(lang=language)  
    if "ner2" in supported_tasks:
        downloader.download("ner2." + language)
    return


if __name__ == '__main__':
    download(lang=LANG)