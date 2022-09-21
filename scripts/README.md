# Notes

## Replace

```sh
# Replace in py via sed script-file
find . -iname '*.py' -exec sed -i -f scripts/replace.sed '{}' +
```

## Rename

```sh
# Move chapters folder
find . -type d -exec rename -n 's|(.*)/in/chapters$|$1/chapters|' '{}' +

# Change vpy extensions
find . -iname '*.vpy' -exec rename '.vpy' '.py' '{}' +

# Move bookmarks
find . -iname '*.bookmarks' -not -path "*/bookmarks/*" -execdir sh -c "mkdir -p bookmarks && mv '{}' bookmarks" \;
```

## Find

```sh
# Find empty files
find . -type f -empty

# Find non-mask png
find . -iname '*.png' -not -path "*/mask/*"

# Find test/old stuff
find . -iname '*pw.py'
find . -iname '*test.py'
find . -type d -iname '*old'

# Find cyrillic symbols
find . -type f -exec grep -IPn "[\p{Cyrillic}]" '{}' +
```
