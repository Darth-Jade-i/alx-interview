#!/bin/bash

read -p "Enter your name: " name
read -p "Enter your email: " email

git config --global user.name "$name"
git config --global user.email "$email"

git config --global --list

# Created by Darth Jade-i
