import attr
from pathlib import Path


@attr.s
class Corpus(object):
    level = attr.ib(validator=attr.validators.instance_of(int))
    words = attr.ib(validator=attr.validators.instance_of(list))
    num_words = attr.ib(validator=attr.validators.instance_of(int))

    @classmethod
    def from_level(cls, level, articles_dir):

        assert level in [0, 1, 2, 3, 4, 5]

        articles_path = Path(articles_dir)
        if not articles_path.exists():
            raise FileNotFoundError(f'Did not find {articles_path}')

        print(f'Looking for articles in {articles_path}')

        words = []
        for path in articles_path.glob(f'*.en.{level}.txt'):
            words_in_file = path.read_text(encoding='utf-8').split()  # does not contain newline characters
            words.extend(words_in_file)
        num_words = len(words)
        return cls(level, words, num_words)