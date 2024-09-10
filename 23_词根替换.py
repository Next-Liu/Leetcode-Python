import collections


def replace(dict, sentence):
    d = collections.defaultdict(set)
    s = collections.defaultdict(int)
    sentence = sentence.split(" ")
    for w in dict:
        d[w[0]].add(w)
        s[w[0]] = max(s[w[0]], len(w))
    for i, w in enumerate(sentence):
        for j in range(s[w[0]]):
            if w[:j + 1] in d[w[0]]:
                sentence[i] = w[:j + 1]
                break
    return ' '.join(sentence)


if __name__ == '__main__':
    dict = ['cat', 'dog']
    sentence = "catter dogger"
    print(replace(dict, sentence))
    l1 = 'cat'
    l2 = {'cat'}
    print(l1 in l2)
    l3 = 'c'
    l4 = {'cat'}
    print(l3 in l4)
