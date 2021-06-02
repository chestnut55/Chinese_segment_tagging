
from tagger.seg import HMMSegger


if __name__ == '__main__':

    # Create an instance
    segger = HMMSegger()
    # Load data
    segger.load_data("../data/train_seg_corpus.txt_utf8")
    # Train
    segger.train()
    test = '我很喜欢自然语言处理'
    res = segger.cut(test)
    print(res)