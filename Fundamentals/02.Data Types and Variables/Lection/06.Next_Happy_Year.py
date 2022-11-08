year = int(input())
happy_year_conditional = False
while not happy_year_conditional:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])
    happy_year_conditional = len(set_year) == len(str(year))
print(year)