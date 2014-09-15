#!/bin/sh

[ -r "./freeze.py" ] && python ./freeze.py && echo 'Site frozen' || echo 'Freezing issue, bailing!' && exit 1
[ -d "./build" ] && git subtree push --prefix ./build origin master && echo 'Site Depolyed' || echo 'Deploy failure' && exit 1 

