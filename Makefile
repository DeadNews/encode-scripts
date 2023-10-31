find_empty_files:
	find . -type f -empty

find_nonmask_png:
	find . -iname '*.png' -not -path "*/mask/*"

find_test_or_old:
	find . -iname '*pw.py'
	find . -iname '*test.py'
	find . -type d -iname '*old'
