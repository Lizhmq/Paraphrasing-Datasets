import random

lines = []
with open("wikianswers/wikianswers-paraphrases-1.0/word_alignments.txt") as f:
    lines = []
    for line in f:
        if random.random() < 0.018:
            lines.append(line.strip())
            if len(lines) == 180000:
                break

lines = [line.replace('\n', ' ').split('\t') for line in lines]
for line in lines:
    assert(len(line) == 3)
pairs = [line[:2] for line in lines]


import random
sampled = random.sample(pairs, len(pairs))
train_data = sampled[:160000]
valid_data = sampled[160000:160000 + 10000]
test_data = sampled[170000:180000]
assert(len(train_data) == 160000)
assert(len(valid_data) == 10000)
assert(len(test_data) == 10000)
def dump(path, data):
    with open(path, 'w') as f:
        for line in data:
            print(line, file=f)
            
dump('wikianswers/wikianswers/train.txt', [' SSEEPP '.join(pairs) for pairs in train_data])
dump('wikianswers/wikianswers/valid.txt', [' SSEEPP '.join(pairs) for pairs in valid_data])
dump('wikianswers/wikianswers/test.txt', [' SSEEPP '.join(pairs) for pairs in test_data])
dump('wikianswers/train_src.txt', [pairs[0] for pairs in train_data])
dump('wikianswers/valid_src.txt', [pairs[0] for pairs in valid_data])
dump('wikianswers/test_src.txt', [pairs[0] for pairs in test_data])
dump('wikianswers/train_tgt.txt', [pairs[1] for pairs in train_data])
dump('wikianswers/valid_tgt.txt', [pairs[1] for pairs in valid_data])
dump('wikianswers/test_tgt.txt', [pairs[1] for pairs in test_data])
