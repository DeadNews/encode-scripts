.PHONY: all clean test default checks pc find

default: checks

install:
	pre-commit install
	poetry install --sync --no-root

update:
	poetry up --latest

checks: pc
pc:
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
