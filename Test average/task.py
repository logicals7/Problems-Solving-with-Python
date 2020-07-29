def average_mark(*marks):
    sum = 0
    count = 0
    for mark in marks:
        sum += mark
        count += 1
    avg = sum / count
    return f'{avg:.1f}'
