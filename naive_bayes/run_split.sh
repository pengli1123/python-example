#!/bin/sh

for (( i = 1; i <= 10; i++ ))
do
    train_data="splits/train${i}"
    test_data="splits/test${i}"

    output="output${i}"

    cmd="./nb_classifier.py ${train_data} ${test_data} > ${output}"
    echo "${cmd}"

    `./nb_classifier.py ${train_data} ${test_data} > ${output}`

done

