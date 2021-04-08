import os
import math
def create_bow(vocab, filepath):
    """ Create a single dictionary for the data
        Note: label may be None
    """
    bow = {}
    f = open(filepath, "r", encoding="utf8")
    #print(vocab)
    vocab = dict.fromkeys(vocab, '0')

    for line in f:
        line = line.strip('\n')
        if line in vocab and line in bow:
            bow[line] += 1
        elif line in vocab and line not in bow:
            bow[line] = 1
        elif line not in vocab and None not in bow:
            bow[None] = 1
        elif line not in vocab and None in bow:
            bow[None] += 1

    f.close()
    return bow


def load_training_data(vocab, directory):
    """ Create the list of dictionaries """
    dataset = []
    dict = {}
    files16 = []
    files20 = []
    for r, d, f in os.walk(directory):
        for file in f:
            if '.txt' in file and '2016' in r:
                files16.append(os.path.join(r, file))
            if '.txt' in file and '2020' in r:
                files20.append(os.path.join(r, file))
    for file in files20:
        dict['label']= '2020'
        dict['bow'] = create_bow(vocab, file)
        dataset.append(dict.copy())
    for file in files16:
        dict['label']= '2016'
        dict['bow'] = create_bow(vocab, file)
        dataset.append(dict.copy())

    return dataset

def create_vocabulary(directory, cutoff):
    """ Create a vocabulary from the training directory
        return a sorted vocabulary list
    """

    vocab = []
    # TODO: add your code here
    #getting txt files in directory, code from
    #https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/

    files = []
    for r, d, f in os.walk(directory):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))


    #creating vocab list
    Dict = {}
    for file in files:
        f = open(file, "r", encoding="utf8")
        for line in f:
            line = line.strip('\n')
            if line in Dict.keys():
                Dict[line] += 1
            else:
                Dict[line] = 1
        f.close()

    for key,value in Dict.items():
        if value >= cutoff:
            vocab.append(key)

    vocab = sorted(vocab)
    #print(vocab)

    return vocab

def prior(training_data, label_list):
    """ return the prior probability of the label in the training set
        => frequency of DOCUMENTS
    """

    smooth = 1 # smoothing factor
    logprob = {}
    # TODO: add your code here
    list16 = 0
    list20 = 0
    total = 0

    #making seperate counts
    for x in training_data:
        total += 1
        if x['label'] == '2016':
            list16 += 1
        elif x['label'] == '2020':
            list20 += 1
    #print(list16)
    #print(list20)
    #16
    prior16 = (list16 + smooth)/(total+2)
    prior20 = (list20 + smooth)/(total+2)

    logprob['2020'] = math.log(prior20)
    logprob['2016'] = math.log(prior16)





    return logprob

def p_word_given_label(vocab, training_data, label):
    """ return the class conditional probability of label over all words, with smoothing """

    smooth = 1 # smoothing factor
    word_prob = {}
    list = []
    yearwords = {}
    wordCountDict = {}
    nonyearwords = {}
    total = 0
    i = 0
    j = 0
    # TODO: add your code here
    #this seperates the dicts from label year into one list and the others in another
    for x in training_data:
        if x['label'] == label:
            yearwords[i] = x['bow']
            i += 1
            #list.append(x)
        else:
            nonyearwords[j] = x['bow']
            j += 1
    #print(nonyearwords)
    #print(yearwords)

    #compiling wordCountDict
    for k,v in yearwords.items():
        for key,value in v.items():
            total += value
            if key in wordCountDict:
                wordCountDict[key] += value
            else:
                wordCountDict[key] = value
    for k,v in nonyearwords.items():
        for key,value in v.items():
            if key in wordCountDict:
                break
            else:
                wordCountDict[key] = 0
    #calculate P for each word in wordCountDict add to word_prob
    if None not in wordCountDict:
        wordCountDict[None] = 0

    for k,v in wordCountDict.items():
        word_prob[k] = math.log(v+smooth*1) - math.log(total + smooth * (len(vocab) +1)))

    return word_prob


##################################################################################
def train(training_directory, cutoff):
    """ return a dictionary formatted as follows:
            {
             'vocabulary': <the training set vocabulary>,
             'log prior': <the output of prior()>,
             'log p(w|y=2016)': <the output of p_word_given_label() for 2016>,
             'log p(w|y=2020)': <the output of p_word_given_label() for 2020>
            }
    """
    retval = {}
    # TODO: add your code here
    vocab = create_vocabulary(training_directory,cutoff)
    training_data = load_training_data(vocab, training_directory)
    priorr = prior(training_data, ['2020', '2016'])
    p16 = p_word_given_label(vocab, training_data, '2016')
    p20 = p_word_given_label(vocab, training_data, '2020')

    retval['vocabulary'] = vocab
    retval['log prior'] = priorr
    retval['log p(w|y=2016)'] = p16
    retval['log p(w|y=2020)'] = p20



    return retval


def classify(model, filepath):
    """ return a dictionary formatted as follows:
            {
             'predicted y': <'2016' or '2020'>,
             'log p(y=2016|x)': <log probability of 2016 label for the document>,
             'log p(y=2020|x)': <log probability of 2020 label for the document>
            }
    """
    retval = {}
    # TODO: add your code here
    #2016


    prior16 = model['log prior']['2016']
    prior20 = model['log prior']['2020']

    f = open(filepath, "r", encoding="utf8")

    lineList = []
    for line in f:
        line = line.strip('\n')
        lineList.append(line)

    #20162016201620162016201620162016
    product = 0
    lineMatch = 0
    for line in lineList:
        for key,value in model['log p(w|y=2016)'].items():
            if line == key:
                product += value
                lineMatch = 1
                break
        if lineMatch == 0:
            product += model['log p(w|y=2016)'][None]
        lineMatch = 0
    #for x in range (0,30):
        #product += model['log p(w|y=2016)'][None]



    p16 =  prior16 + product
    #print(p16)

    #202020202020202020220202022020202
    product2 = 0
    lineMatch2 = 0
    for line in lineList:
        for k,v in model['log p(w|y=2020)'].items():
            if line == k:
                product2 += v
                lineMatch2 = 1
                break
        if lineMatch2 == 0:
            product2 += model['log p(w|y=2020)'][None]
        lineMatch2 = 0

    p20 =  prior20 + product2


    #####test_train
    pre = 0
    if p20 > p16:
        pre = '2020'
    else:
        pre = '2016'


    retval['predicted y'] = pre
    retval['log p(y=2016|x)'] = p16
    retval['log p(y=2020|x)'] = p20

    return retval


