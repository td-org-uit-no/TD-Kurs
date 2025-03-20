import numpy as np
import os

nchars = 25
alphabet = [chr(ord('a') + i) for i in range(nchars)]
alphabet += [chr(ord('A') + i) for i in range(nchars)]

def concat_char_list(charlist: list[str]):
    outputstr = ''
    for c in charlist:
        outputstr += c
    return outputstr

def fname(alphabet: list, min_len=4, max_len=14, extension:str = 'txt'):
    namelength = np.random.randint(min_len, max_len)
    filename = np.random.choice(alphabet, namelength)
    filename = concat_char_list(filename)
    return f"{filename}.{extension}"


def write_random_junk_to_file(filename: str):

    if os.path.exists(filename): return
    writealphabet = alphabet + [" "]
    file_content_length = np.random.randint(1000, 5000)
    contents = concat_char_list(np.random.choice(writealphabet, file_content_length))

    with open(filename, 'w') as f:
        f.write(contents)

number_of_files = 50

for _ in range(number_of_files):
    filename = fname(alphabet)
    write_random_junk_to_file(filename)


