def gen():
    for c in 'AB':
        yield c

print(list(gen()))

def gen_new():
    yield from 'ABc'

print(list(gen_new()))