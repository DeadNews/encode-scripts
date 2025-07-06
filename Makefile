.PHONY: all clean default install lock update check pc test docs run

default: check

install:
	pre-commit install
	uv sync
update:
	uv sync --upgrade

check: pc
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
