study_hours = {}

with open("HW_6.txt", encoding="utf-8") as f:
    for line in f:
        theme, hours = line.split(':')
        sum_of_hours = sum(map(int, "".join([i for i in hours if i == ' ' or ('0' <= i <= '9')]).split()))
        study_hours[theme] = sum_of_hours

print(f"{study_hours}")