#!/bin/bash

mkdir linux_practice
cd linux_practice
mkdir name permission
cd name
touch file1.txt
touch file2.txt
cd ../permission
touch file3.txt
touch file4.txt
cd ../name
rm file1.txt
mv file2.txt show.txt
echo "Hello linux" > temp.txt && cat show.txt >> temp.txt && mv temp.txt show.txt
cat show.txt
cd ..
chmod 644 permission/*
echo "Changed permissions for file3.txt to -rw-r--r--"
echo "Changed permissions for file4.txt to -rw-r--r--"
