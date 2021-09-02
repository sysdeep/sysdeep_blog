#!/bin/bash


BLOG_PATH=../sysdeep.github.io
CONTENT_PATH=./output

# If a command fails then the deploy stops
set -e


printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

make clean
make html

rsync -avz --delete --exclude ".git"  $CONTENT_PATH/* $BLOG_PATH


cd $BLOG_PATH

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master