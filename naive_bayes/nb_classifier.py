#!/usr/local/bin/python

import sys; #sys.argv
import re; #regex
import math; #log, abs

if len(sys.argv) != 3:
    print "Usage: nb_classifier split1.train split.test"
    exit()

train_data = sys.argv[1];
test_data = sys.argv[2];

#data_path = '/afs/andrew.cmu.edu/user16/pengfeil/10601/hwk8/python_example'
data_path = './data'

labels = ['atheism','auto','baseball',  'christian' , 'crypt' , 'electronics' , 'graphics' , 'guns' , 'hockey' , 'ibm' , 'mac' , 'medical' , 'mideast' , 'motorcycles' , 'politics' , 'religion' , 'sale' , 'space' , 'windows' , 'winx']

vocab = set();
docs = dict();

prob = dict();
cond_prob = dict();

total_examples = 0;

#initialize docs
for label in labels:
    docs[label] = list();

#collect all words
train_file = open(train_data, 'r');

for file in train_file:
        file_fd = open(data_path + '/' + file.rstrip('\n'), 'r')

        words = file_fd.read().split(' ');

        for w in words:
            if w.isalpha(): #only add words that's are in alphabetic
                vocab.add(w.lower());

        #find the label 
        #this should be in step 2 but combine in here for efficiency
        label = re.search('^([a-z]+?)[0-9]*\.txt', file.rstrip('\n')).group(1); 
        docs[label].append(file);

        file_fd.close();
        total_examples = total_examples + 1.0;

train_file.close();

vocab_len = len(vocab);

train_file = open(train_data, 'r');

#calculate the P(label) and P(word|label)
for label in labels:

    text = [];
    prob[label] = len(docs[label]) / total_examples;

    for file in docs[label]:
        file_fd = open(data_path + '/' + file.rstrip('\n'), 'r');

        words = file_fd.read().split(' ');
        for w in words:
            if w.isalpha():
                text.append(w.lower());

        file_fd.close();

    distinct_word = len(set(text));

    for word in vocab:
        word_time = text.count(word);
        cond_prob[word + '|' + label] = (word_time + 1.0) / (distinct_word + vocab_len);

train_file.close();

test_file  = open(test_data, 'r');

#classify the test files
for file in test_file:
    pos = [];

    file_fd = open(data_path + '/' + file.rstrip('\n'), 'r');
    words = file_fd.read().split(' ');

    for w in words:
        if w.isalpha() and w.lower() in vocab:
            pos.append(w.lower());

    max = -1.0 * sys.maxint;
    ans = 'NONE';

    for label in labels:
        tmp = 0.0;
        
        for word in pos:
            tmp = tmp + math.log(cond_prob[word + '|' + label]);

        tmp = tmp + math.log(prob[label]);
        
        #now that we take abs(log(x)), we want the smaller ones
        if tmp > max:
            ans = label;
            max = tmp;

    print file.rstrip('\n') + ' ' + ans;

test_file.close();

