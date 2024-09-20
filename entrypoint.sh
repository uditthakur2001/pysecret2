#!/bin/sh

# Check if the first argument is a git repository URL or a file path
if [ -n "$1" ]; then
    trufflehog --regex --rules rules.json $1
else
    echo "Please provide a git repository URL or file path."
    exit 1
fi
