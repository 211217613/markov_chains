#!/opt/anaconda/

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n\n', ' ')
    return contents