# Notes

## Replace

```sh
# Replace in py|vpy via sed script-file
find . -regextype egrep -iregex ".*\.(py|vpy)$" -exec sed -i -f scripts/replace.sed '{}' +

# Replace in py|vpy via py script
find . -regextype egrep -iregex ".*\.(py|vpy)$" -exec scripts/replace_maps.py '{}' +
```

## Rename

```sh
# Move chapters folder
find . -type d -exec rename -n 's|(.*)/in/chapters$|$1/chapters|' '{}' +

# Change vpy extensions
find . -type f -iname '*.vpy' -exec rename '.vpy' '.py' '{}' +

# Move bookmarks
find . -type f -iname '*.bookmarks' -not -path "*/bookmarks/*" -execdir sh -c "mkdir -p bookmarks && mv '{}' bookmarks" \;
```

## Find

```sh
# Find empty files
find . -type f -empty

# Find non-mask png
find . -iname '*.png' -not -path "*/mask/*"

# Find test/old stuff
find . -iname '*pw.vpy'
find . -iname '*test.vpy'
find . -type d -iname '*old'

# Find cyrillic symbols
find . -type f -exec grep -IPn "[\p{Cyrillic}]" '{}' +
```
