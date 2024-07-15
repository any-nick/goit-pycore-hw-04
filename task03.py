import sys
from pathlib import Path
from colorama import Fore

def print_file_structure(dir_to_print, depth=0):
    directory = Path(dir_to_print)
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{"\t"*depth} {Fore.BLUE} {item.name}/ {Fore.RESET}")
            #Print directory sctucture within recurcive method
            print_file_structure(item, depth + 1)
        else:
            print(f"{"\t"*depth} {Fore.GREEN} {item.name} {Fore.RESET}")

def main ():
    #Check if entered path is a directory and exists on filesystem
    if Path(sys.argv[1]).is_dir() and Path(sys.argv[1]).exists:
        print_file_structure(Path(sys.argv[1]))
    else:
        print("Entered path is not a directory or does not exists")

if __name__ == "__main__":
    main()