from src.Models.characters_models import Characters


class CharactersSerializer:
    def __init__(self, character: Characters):
        self.name = character.name
        self.status = character.status
        self.reputation = character.reputation
        self.bounty = character.bounty
        self.gender = character.gender

