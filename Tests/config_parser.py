from pathlib import Path

class ParseConfig:
    # TODO made better parser curently mocked

    def __init__(self, path):
        self.path = Path(__file__).parents[1]
        self.set = 'PuzzleSet_3' # hardcoded
