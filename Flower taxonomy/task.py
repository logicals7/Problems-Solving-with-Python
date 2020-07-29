iris = {}
def add_iris(id_n, species, petal_length, petal_width, **others):
    iris[id_n] = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    for feature, value in others.items():
        iris[id_n][feature] = value
    return iris


