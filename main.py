#!/opt/anaconda3/bin/python
import argparse
import random


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

def generate_message(chain, count = 10):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    return message

def write_file(filename, message):
    with open(filename, 'w') as file:
        file.write(message)

def main():
    con = read_file('input.txt')
    chain = build_chain(con)
    message = generate_message(chain)
    print(message)

    

if __name__ == '__main__':
    main()