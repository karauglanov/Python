import re
my_st = "10 - Санкт-Петербург 1 - (30.447;59.912).xlsx"
st = re.split(" - ", my_st)
n = st[0]
naz = st[1]
print(n, naz, sep='\n')