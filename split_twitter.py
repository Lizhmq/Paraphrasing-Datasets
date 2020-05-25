import pandas
data = []
true_data = []
with open('twitter/2016_Oct_10--2017_Jan_08_paraphrase.txt', 'r') as f:
    for line in f.readlines():
        pair = line.strip().split('\t')
        assert(len(pair) == 2)
        src, tgt = pair
        true_data.append((src, tgt))
            
            
data_pairs = true_data
# 110-1-3 following the setting of RLv.s.IL
import random
sampled = random.sample(data_pairs, len(data_pairs))
train_data = sampled[:110000]
valid_data = sampled[110000:110000 + 1000]
test_data = sampled[111000:114000]

def dump(path, data):
    with open(path, 'w') as f:
        for line in data:
            print(line, file=f)
            
dump('twitter/twitter/train.txt', [' SSEEPP '.join(pairs) for pairs in train_data])
dump('twitter/twitter/valid.txt', [' SSEEPP '.join(pairs) for pairs in valid_data])
dump('twitter/twitter/test.txt', [' SSEEPP '.join(pairs) for pairs in test_data])

dump('twitter/train_src.txt', [pairs[0] for pairs in train_data])
dump('twitter/valid_src.txt', [pairs[0] for pairs in valid_data])
dump('twitter/test_src.txt', [pairs[0] for pairs in test_data])

dump('twitter/train_tgt.txt', [pairs[1] for pairs in train_data])
dump('twitter/valid_tgt.txt', [pairs[1] for pairs in valid_data])
dump('twitter/test_tgt.txt', [pairs[1] for pairs in test_data])
