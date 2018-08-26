class Allergies(object):

    ITEM_SCORES = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return bool(self.ITEM_SCORES[item] & self.score)

    @property
    def lst(self):
        return list(item for item in self.ITEM_SCORES if self.is_allergic_to(item))
