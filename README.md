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
" occured 271 times at 49.72%
, occured 88 times at 16.15%
} occured 46 times at 8.44%
{ occured 46 times at 8.44%
_ occured 19 times at 3.49%
' occured 15 times at 2.75%
= occured 15 times at 2.75%
. occured 14 times at 2.57%
\ occured 13 times at 2.39%
# occured 10 times at 1.83%
- occured 5 times at 0.92%
+ occured 3 times at 0.55%


NUMBERS
0 occured 38 times at 61.29%
1 occured 16 times at 25.81%
2 occured 4 times at 6.45%
9 occured 1 times at 1.61%
8 occured 1 times at 1.61%
7 occured 1 times at 1.61%
6 occured 1 times at 1.61%
```

### Extra

I have included a script to combine files it will combine any files that are put into the 'files to combine folder' the combined file will be output in the same directory as 'file combiner.py'.
