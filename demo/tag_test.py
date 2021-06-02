from tagger.tagging import PosTagging

if __name__ == '__main__':

    # Create an instance
    pt = PosTagging()
    # Load data
    pt.processCorpus("../data/199801.txt")
    test = ['我', '很', '喜欢', '自然', '语言', '处理']
    res = pt.predictTag(test)
    print(res)