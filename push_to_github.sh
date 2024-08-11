#!/bin/bash

git add .

echo "What are you sending to Github?"
read -p "Reply with : repo, dir, file or dir & file" type
read -p "Enter your commit message: " message

git commit -m "$type: $message"
git push

echo "You do know you're the greatest koder"
# Created by Darth Jade-i
