from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn


def tag(sentence):
    words = word_tokenize(sentence)
    words = pos_tag(words)
    return words


def paraphraseable(tag):
    return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ')


def pos(tag):
    if tag.startswith('NN'):
        return wn.NOUN
    elif tag.startswith('V'):
        return wn.VERB


def synonyms(word, tag):
    lemma_lists = [ss.lemmas() for ss in wn.synsets(word, pos(tag))]
    lemmas = [lemma.name() for lemma in sum(lemma_lists, [])]
    return set(lemmas)


def synonymIfExists(sentence):
    for (word, t) in tag(sentence):
        if paraphraseable(t):
            syns = synonyms(word, t)
            if syns:
                if len(syns) > 1:
                    yield [word, list(syns)]
                    continue
        yield [word, []]


def paraphrase(sentence):
    return [x for x in synonymIfExists(sentence)]


paraset = paraphrase("The quick brown fox jumps over the lazy dog")
print(paraset)
for (word, syn) in paraset:
    word = pos_tag([word])
    syn = pos_tag(syn)
    print(word[0][0], word[0][1])
    for item, type in syn:
        print(item, type, end="; ")
    print("------------------")

# https://medium.com/analytics-vidhya/pos-tagging-using-conditional-random-fields-92077e5eaa31
