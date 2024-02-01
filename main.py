import os.path

if not os.path.exists("tables.txt"):
    f = open("tables.txt","x")
    f.close()
    print("Creating tables.")
else:
    print("Table exist.")
    quit()

f = open("tables.txt","w")
f.write("TIMES TABLES:")
f.write("\n------------------------------------")

for n in range(1,13):
    f.write(f"\n The {n} times tables:")
    for m in range(1,13):
        a = n*m
        question = f"\n {n} X {m} = {a}"
        f.write(question)
    f.write("\n------------------------------------")

f.close()
quit()