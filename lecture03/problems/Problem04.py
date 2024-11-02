from markdown_it.rules_block import paragraph


def solution() -> str:
    paragraph: str = "\"Python is a great language!\", said Fred. \"I don't ever remember having this much fun before.\" "
    return paragraph

def solution_one() -> str:
    paragraph: str = '"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."'
    return paragraph


if __name__ == '__main__':
    txt = solution()
    print(txt)
    txt = solution_one()
    print(txt)
    


