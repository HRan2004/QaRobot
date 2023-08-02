from chatterbot import ChatBot
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_random_response

from spacy.tokenizer import Tokenizer
import spacy


class SpacyAdapter:

    class_name = 'SpacyAdapter'

    def __init__(self, **kwargs):
        self.nlp = spacy.load("zh_core_web_sm")
        self.tokenizer = Tokenizer(self.nlp.vocab)

    def can_process(self, _=None):
        return True

    def process(self, statement, args):
        doc = self.nlp(statement.text)
        statement.entities = {}
        statement.keywords = []

        for ent in doc.ents:
            statement.entities[ent.label_] = ent.text

        for noun_chunk in doc:
            statement.keywords.append(noun_chunk.text)
        return {}


chatbot = ChatBot(
    '对话机器人',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': levenshtein_distance,
            'response_selection_method': get_random_response
        }
    ]
)
chatbot.logic_adapters.append(SpacyAdapter())

