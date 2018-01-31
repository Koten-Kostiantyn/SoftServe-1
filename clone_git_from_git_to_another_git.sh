#!/bin/bash
echo $1
# rm -rf $1.git
git clone --mirror git@$GIT_FIRST/$1.git
cd $1.git
git remote set-url origin git@$GIT_SECOND/$1.git
git push -f origin
cd ..

