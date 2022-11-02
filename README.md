# Most Used Key Counter

### Setup

Inside of 'most used key counter.py' change file_path to the path of the file you want to check. Make an array following the array example, and at the bottom of the file call the mostUsedCharactersCounter() which takes 2 parameters a string of a name for the characters you are checking and then an array.

### Array Example

The array must follow the format below changing anything but the character value will break the script

```
example_array = [
    {"character": "!", "count": 0},
    {"character": "@", "count": 0},
    {"character": "#", "count": 0},
    {"character": "$", "count": 0},
    {"character": "%", "count": 0}
]
```

### Function Call Example

```
mostUsedCharactersCounter('Example Name of Characters', example_array)
```

### Example Output

```
SYMBOLS
" occurred 271 times at 49.72%
, occurred 88 times at 16.15%
} occurred 46 times at 8.44%
{ occurred 46 times at 8.44%
_ occurred 19 times at 3.49%
' occurred 15 times at 2.75%
= occurred 15 times at 2.75%
. occurred 14 times at 2.57%
\ occurred 13 times at 2.39%
# occurred 10 times at 1.83%
- occurred 5 times at 0.92%
+ occurred 3 times at 0.55%


NUMBERS
0 occurred 38 times at 61.29%
1 occurred 16 times at 25.81%
2 occurred 4 times at 6.45%
9 occurred 1 times at 1.61%
8 occurred 1 times at 1.61%
7 occurred 1 times at 1.61%
6 occurred 1 times at 1.61%
```

### Extra

I have included a script to combine files it will combine any files that are put into the 'files to combine folder' the combined file will be output in the same directory as 'file combiner.py'.
