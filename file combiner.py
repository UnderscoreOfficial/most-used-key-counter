from pathlib import Path

# combines all files in 'files to combine' folder outputs new file to the current directory

file_name = str(input('Enter name for combined file: '))

with open(f'{file_name}.txt', 'w') as file:
    for i in Path('files to combine\\.').iterdir():
        if i.is_file():
            file.write(i.read_text())
