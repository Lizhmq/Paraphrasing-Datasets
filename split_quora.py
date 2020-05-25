import pandas

with open("quora/quora_duplicate_questions.tsv") as f:
    data = pandas.read_csv(f, delimiter='\t')

true_data = data[data['is_duplicate'] == 1]
src = list(true_data['question1'])
tgt = list(true_data['question2'])
data_pairs = list(zip(src, tgt))

# 100-3-30 following the setting of RLv.s.IL
import random
sampled = random.sample(data_pairs, len(data_pairs))
train_data = sampled[:100000]
valid_data = sampled[100000:100000 + 3000]
test_data = sampled[103000:133000]

def dump(path, data):
    with open(path, 'w') as f:
        for line in data:
            print(line, file=f)
            
dump('quora/quora/train.txt', [' SSEEPP '.join(pairs) for pairs in train_data])
dump('quora/quora/valid.txt', [' SSEEPP '.join(pairs) for pairs in valid_data])
dump('quora/quora/test.txt', [' SSEEPP '.join(pairs) for pairs in test_data])
dump('quora/train_src.txt', [pairs[0] for pairs in train_data])
dump('quora/valid_src.txt', [pairs[0] for pairs in valid_data])
dump('quora/test_src.txt', [pairs[0] for pairs in test_data])
dump('quora/train_tgt.txt', [pairs[1] for pairs in train_data])
dump('quora/valid_tgt.txt', [pairs[1] for pairs in valid_data])
dump('quora/test_tgt.txt', [pairs[1] for pairs in test_data])

