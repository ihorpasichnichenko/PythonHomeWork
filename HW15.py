import pickle

def append_dict_file(filename, slovar):
    with open('result.json', 'rb') as f:
        united = pickle.load(f)
    united.update(slovar)
    with open('result.json', 'wb') as f:
        pickle.dump(united, f)

A = {"кира" : 1}
B = {"валера" : 2}


with open('result.json', 'wb') as f:
    pickle.dump(A, f)

append_dict_file('result.json', B)


with open('result.json', 'rb') as f:
    slovari = pickle.load(f)
    print((slovari))