.PHONY: all clean test checks find

install-all: install pc-install

install:
	poetry install --sync

pc-install:
	pre-commit install

update-latest:
	poetry up --latest

checks: pc-run

pc-run:
	pre-commit run -a

find: find-empty find-nonmask find-test find-old

find-empty:
	find . -type f -empty

find-nonmask:
	find . -iname '*.png' -not -path "*/mask/*"

find-test:
	find . -iname '*pw.py'
	find . -iname '*test.py'

find-old:
	find . -type d -iname '*old'
