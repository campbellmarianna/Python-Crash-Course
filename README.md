# Python Crash Course Reference

## Strings
- to add a table to your text use the character combination `\t`

Example:
```
>>> print("\tPython")
	Python
```

- to add a new line to your string use the character combination `\n`

Example:
```
>>> print("Language: \nPython\nC\nJavaScript")
Language:
Python
C
JavaScript
```

- to tell Python to move to a new line, and start the next line with a tab

```
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
	Python
	C
	JavaScript
```
## Lists

To access an item in a list we use index notation starting at index 0. Furthermore, index -1 asks Python to give us the last item in a given list

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```
