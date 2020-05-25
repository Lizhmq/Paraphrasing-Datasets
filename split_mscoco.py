import json
path1 = 'mscoco/annotations/captions_train2014.json'
path2 = 'mscoco/annotations/captions_val2014.json'

with open(path1, 'r') as f:
    data = json.load(f)
res = dict()
for item in data['annotations']:
    if item['image_id'] in res.keys():
        res[item['image_id']].append(item['caption'].replace('\n', ' '))
    else:
        res[item['image_id']] = [item['caption'].replace('\n', ' ')]
with open(path2, 'r') as f:
    data = json.load(f)
for item in data['annotations']:
    if item['image_id'] in res.keys():
        res[item['image_id']].append(item['caption'].replace('\n', ' '))
    else:
        res[item['image_id']] = [item['caption'].replace('\n', ' ')]
        
        
import random

pairs = []
for item in res.values():
    captions = random.sample(item, 4)
    pairs.append(captions[:2])
    pairs.append(captions[2:4])
    
import random
sampled = random.sample(pairs, len(pairs))
train_data = sampled[:160000]
valid_data = sampled[160000:160000 + 5000]
test_data = sampled[165000:175000]
assert(len(train_data) == 160000)
assert(len(valid_data) == 5000)
assert(len(test_data) == 10000)
def dump(path, data):
    with open(path, 'w') as f:
        for line in data:
            print(line, file=f)
            
dump('mscoco/mscoco/train.txt', [' SSEEPP '.join(pairs) for pairs in train_data])
dump('mscoco/mscoco/valid.txt', [' SSEEPP '.join(pairs) for pairs in valid_data])
dump('mscoco/mscoco/test.txt', [' SSEEPP '.join(pairs) for pairs in test_data])
dump('mscoco/train_src.txt', [pairs[0] for pairs in train_data])
dump('mscoco/valid_src.txt', [pairs[0] for pairs in valid_data])
dump('mscoco/test_src.txt', [pairs[0] for pairs in test_data])
dump('mscoco/train_tgt.txt', [pairs[1] for pairs in train_data])
dump('mscoco/valid_tgt.txt', [pairs[1] for pairs in valid_data])
dump('mscoco/test_tgt.txt', [pairs[1] for pairs in test_data])
