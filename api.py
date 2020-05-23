import os
import json

import responder

from download import download
from ner import NERer


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']
LIBRARY = env.get('LIBRARY')
LANG = env.get('LANG')

api = responder.API(debug=DEBUG)
if LIBRARY == 'polyglot':
    download(lang=LANG)    
nerer = NERer(library=LIBRARY, lang=LANG)


@api.route("/")
async def process(req, resp):
    body = await req.text
    texts = json.loads(body)
    docs = [nerer.recognize(text) for text in texts]
    resp.media = dict(data=docs)


if __name__ == "__main__":
    api.run()