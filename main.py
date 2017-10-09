#!/opt/anaconda/

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n\n', ' ')
    return contents

def build_chain(text, chain={}):
    words = text.split(' ')
    index = 1
    for word in words[1::]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    return chain