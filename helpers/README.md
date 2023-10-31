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
# Find cyrillic symbols
find . -type f -exec grep -IPn "[\p{Cyrillic}]" '{}' +
```
