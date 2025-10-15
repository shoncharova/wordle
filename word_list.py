#word_list
import pathlib as p
import sys
from string import ascii_letters as ASC
in_path = p.Path(sys.argv[1])
out_path = p.Path(sys.argv[2])
words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding='utf-8').split()
        if all(letter in ASC for letter in word) #this will only add the word if all leters are ASCII
    },
    key = lambda word:(len(word), word), #how to customise the order of words. Here: first, the length of the word, next the letter
)
out_path.write_text('\n'.join(words))
#shell : python word_list.py 5LW.txt wordlist.txt
# 1 - program to run, 2 - which file to scan, 3 - where to write