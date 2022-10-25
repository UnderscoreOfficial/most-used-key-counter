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
" occured 271 times at 37.38%
, occured 88 times at 12.14%
} occured 46 times at 6.34%
{ occured 46 times at 6.34%
) occured 23 times at 3.17%
( occured 23 times at 3.17%
_ occured 19 times at 2.62%
\ occured 13 times at 1.79%
# occured 10 times at 1.38%
- occured 5 times at 0.69%
+ occured 3 times at 0.41%
? occured 1 times at 0.14%


NUMBERS
0 occured 49 times at 75.38%
1 occured 5 times at 7.69%
2 occured 4 times at 6.15%
9 occured 1 times at 1.54%
8 occured 1 times at 1.54%
7 occured 1 times at 1.54%
```

### Extra

I have included a script to combine files it will combine any files that are put into the 'files to combine folder' the combined file will be output in the same directory as 'file combiner.py'.
