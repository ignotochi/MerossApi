from json import JSONEncoder


class OutcomeJsonEncoder(JSONEncoder):
    def default(self, item):
        return item.__dict__
