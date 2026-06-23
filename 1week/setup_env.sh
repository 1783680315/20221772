#!/bin/bash
git config --global user.name "student"
git config --global user.email "student@example.com"
ssh-keygen -t ed25519 -C "student@example.com"
echo "Environment ready"
