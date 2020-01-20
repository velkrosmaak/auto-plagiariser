from nltk.corpus import wordnet
import nltk
import re

# print("Downloading wordnet resources...")
# nltk.download('wordnet')

synonyms = []


def get_synonym(inputword):
    synonyms = []
    try: # try it, if there's an error just pass the inputword through
        for syn in wordnet.synsets(inputword):
            for l in syn.lemmas():
                if l.name() not in synonyms and l.name() is not inputword:
                    synonyms.append(l.name())            
        try:
            return((synonyms[-1]))
        except:
            return inputword
    
    except Exception as e:
        print (e)
        return inputword
    
    
def read_file(inputfile):
    print("Reading", inputfile)
    f = open(inputfile).read()
    # plain_text = re.sub(r'[^\w]', ' ', f)
    plain_text = f
    individual_words = []
    for word in plain_text.split():
        # do something with word
        individual_words.append(word)
    return individual_words


def write_output(original_word, new_word, filename):
    f = open(filename, "a")
    f.write((new_word + f"({original_word}) "))
    f.close()


def write_output_pure(new_word, filename):
    f = open(filename, "a")
    f.write((new_word + " "))
    f.close()

    
def replace_word(inword):
    new_word = inword.replace(inword, get_synonym(inword))
    return new_word

filename = "quick.txt"
        
all_words = read_file(filename)
for words in all_words:
    syn = (get_synonym(words))
    # write_output(words, syn, "output.txt")
    write_output_pure(syn, filename + "_output.txt")
    syn2 = (replace_word(words))
    write_output_pure(syn, filename + "_output_b.txt")

    print(words, syn, syn2)