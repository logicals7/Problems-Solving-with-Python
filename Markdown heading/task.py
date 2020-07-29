def heading(word, level=1):
    if level <= 1:
        return f'# {word}'
    if level == 2:
        return f'## {word}'
    if level == 3:
        return f'### {word}'
    if level == 4:
        return f'#### {word}'
    if level == 5:
        return f'##### {word}'
    return f'###### {word}'