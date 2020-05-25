## Paraphrasing Datasets

这个仓库包含了学术界常用的英文paraphrasing generation（复述生成）的数据集：Quora, Twitter, MSCOCO, WikiAnswers.

#### Quora

Quora数据集是从Quora问答社区收集的问题对，数据来源于[Kaggle 竞赛](https://www.kaggle.com/c/quora-question-pairs)，训练集共包含404,290个问题对（见quora_duplicate_questions.tsv），包含标签is_duplicate，其中正例约155k对，可用作paraphrase generation的数据集。

#### Twitter

[Twitter URL Corpus](https://github.com/lanwuwei/Twitter-URL-Corpus)数据来自用户发表的Twitter内容，由论文"A Continuously Growing Dataset of Sentential Paraphrases"整理提出，数据包括2016.10-2017.1的数据和2017一年数据（2,869,657对）两部分，一年数据没有标签，给出了在三月数据上训练的paraphrase识别模型预测的概率，可以自己设定阈值筛选paraphrases。在paraphrase generation生成任务上主要使用三月数据的正例部分（114,025对）。

#### MSCOCO

MSCOCO数据集来源于2014年的[Image Caption](http://cocodataset.org/#download)任务，原始数据包含Train14(82k)和Val14(40k)共122k张图片，每个图片有5条描述，每张图片的描述可以随机组成两对paraphrase，共244k对.

#### WikiAnswers

WikiAnswers数据集由论文"Paraphrase-Driven Learning for Open Question Answering"提出（见[Paralex](http://knowitall.cs.washington.edu/paralex/)），包含语义类似的问题对，数据集设定类似于Quora。数据集较大，含18M word-aligned问题对。训练时经常使用lemmatized的句子(e.g are->be)，随机选取一部分（如4.8M or 2.8M）。

#### Script

仓库包含了[Summarization](https://github.com/abisee/cnn-dailymail)任务提供的数据处理脚本-make_datafiles.py，按照需要进行了一些修改。功能是分词、将数据集处理成tensorflow容易处理的格式并按1k的大小分割。使用需要下载Stanford CoreNLP包，详情见[Summarization](https://github.com/abisee/cnn-dailymail)。使用时可根据自行需要修改make_datafile.py中的get_art_abs函数。
运行方式：
```
python make_datafiles.py <data_dir> <output_dir>
e.g.
	python make_datafiles.py mscoco/mscoco mscoco/processed
```

#### 数据描述

这里给出了Quora, Twitter, MSCOCO的全部数据，由于WikiAnswers数据较大，只给出了随机选取的部分，如有需要可以到给出的链接下载。

总的来说，Quora的数据质量较高，Twitter和WikiAnswers的数据更杂乱一些，MSCOCO语料质量尚可，但是由于MSCOCO是不同人对一张图片的描述，所以复述关系可能不能直接体现。

子目录中包含了预处理过的数据，其中Twitter选取的是三月数据，按照以下大小划分：

| Dataset | Train | Val | Test |
| --- | --- | --- | --- |
| Quora | 100k | 3k | 30k |
| Twitter | 110k | 1k | 3k |
| MSCOCO | 160k | 5k | 10k |
| WikiAnswers | 160k | 10k | 10k |

(train/valid/test)_(src/tgt).txt是分开的的数据，每行一条，src与tgt对应，(train/valid/test).txt则同时包含src和tgt，每行用"SSEEPP"分开；(train/val/test).bin和vocab是经过tensorflow处理的数据，使用见[Pointer-Generator](https://github.com/abisee/pointer-generator)。