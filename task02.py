
def clean_data(loaded_data: list[str]):
    data = []
    for raws in loaded_data:
        data.append(raws.strip().split(","))
    return data

def get_cats_info(path:str):
    cats_dictionary = []
    #Data loading
    try:
        with open(path, "r", encoding="utf-8") as file:
            loaded_data = file.readlines()
    except FileNotFoundError:
        return "File Not Found"
    except UnicodeDecodeError:
        print("The file is possibly corrupted")
    
    #Data cleaning
    cats_list = clean_data(loaded_data)

    #Setting dictionary
    for cat in cats_list:
        cat = {
                "id": cat[0],
                "name": cat[1],
                "age": cat[2]
            }
        cats_dictionary.append(cat)
    return cats_dictionary

def main ():
    cats_info = get_cats_info("cats.txt")
    print(cats_info)

if __name__ == "__main__":
    main()