
def clean_data(salary_data: list[str]):
    data:float =[]
    for raws in salary_data:
        data.append(float(raws.strip().split(",")[1]))
    return data

def total_salary(path:str):
    #Data loading
    try:
        with open(path, "r", encoding="utf-8") as file:
            loaded_data = file.readlines()
    except FileNotFoundError:
        return "File Not Found"
    except UnicodeDecodeError:
        print("The file is possibly corrupted")
    
    #Data cleaning
    salaries = clean_data(loaded_data)

    #Data calculation
    salary_sum = round(sum(salaries),2)
    salary_avg = round(sum(salaries) / len(salaries),2)
    result = (salary_sum,salary_avg)
    return result

def main ():
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()