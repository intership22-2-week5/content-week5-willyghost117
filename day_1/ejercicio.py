from functools import reduce
DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'internship',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #global DATA
    # Comprehensions solutions
    # 1. obtener todos los desarrolladores de python
    #print(list(filter(lambda item: item['language'] == 'python', DATA)))
    #py1 = reduce(lambda item: item['language'] == 'python', DATA)
    #print(p1)
    #py = list(map(lambda item: item['language'] == 'python', DATA))
    #print(py)
    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
    #print(list(filter(lambda item: item['language'] == 'python'and item['age'] > 20 , DATA)))
    # 3. obtener todos los trabajadores de ciancoders 
    #print(list(filter(lambda item: item['organization'] == 'Ciancoders', DATA)))
    
    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
    #print(list(filter(lambda item: item['organization'] == 'Ciancoders' and item['age'] > 30, DATA)))
    # 5. obtener todos los trabajadores de mayores de 18 años
    print(list(filter(lambda item: item['age'] > 18, DATA)))
    #py1 = reduce(lambda item: item['age'] > '18', DATA)
    py = list(map(lambda item: item['age'] > 18, DATA))
    print(py)
    #print (py1)
    # 6. obtener todos los trabajadores de mayores a 70 años
    #print(list(filter(lambda item: item['age'] > 70, DATA)))
    pass

if __name__ == '__main__':
    run()