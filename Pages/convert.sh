#!/bin/bash

# Convert the LPTHW pages into PDF so can read offline

for f in {1..52}
do
	echo "Doing "$f
	wkpdf --source http://learnpythonthehardway.org/book/ex$f.html --output $f.pdf --paper a4
done
