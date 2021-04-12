# studenti

import pandas
studenti1 = pandas.read_csv("studenti1.csv")
#print(studenti1)
studenti2 = pandas.read_csv("studenti2.csv")
#print(studenti2)
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
print(studenti)
From Aleš Hura to Everyone:  08:19 PM
# studenti

import pandas
studenti1 = pandas.read_csv("studenti1.csv")
#print(studenti1)
studenti2 = pandas.read_csv("studenti2.csv")
#print(studenti2)
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
#print(studenti)

# 2
#print( studenti["ročník"].isnull() )
print( studenti["ročník"].isnull().shape  )
print( studenti[studenti["ročník"].isnull()].shape  )

print( studenti.columns  )
print( studenti[studenti["kruh"].isnull()].shape  )
From Aleš Hura to Everyone:  08:32 PM
---------------------------------------
import pandas
studenti1 = pandas.read_csv("studenti1.csv")
#print(studenti1)
studenti2 = pandas.read_csv("studenti2.csv")
#print(studenti2)
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
#print(studenti)

# 3
studenti = studenti.dropna()

print(  studenti.shape  )
----------------------------------------
# studenti

import pandas
studenti1 = pandas.read_csv("studenti1.csv")
#print(studenti1)
studenti2 = pandas.read_csv("studenti2.csv")
#print(studenti2)
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
#print(studenti)

# 4
studenti = studenti.dropna()
print(  studenti.shape  )
print(  studenti.groupby("obor").count()  )
--------------------------------
# studenti

import pandas
studenti1 = pandas.read_csv("studenti1.csv")
#print(studenti1)
studenti2 = pandas.read_csv("studenti2.csv")
#print(studenti2)
studenti = pandas.concat([studenti1, studenti2], ignore_index=True)
#print(studenti)


# 4
studenti = studenti.dropna()
studenti.shape
studenti.groupby("obor").count()

# 5
print(  studenti.groupby("obor")["prospěch"].mean()  )

# 6
import pandas
studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")
studenti = pandas.concat([studenti1, studenti2])
studenti = studenti.dropna()
jmena = pandas.read_csv("jmena.csv")

# 7
pandas.merge(studenti, jmena, on=["jméno"])
studenti.shape
studentiPlusJmena = pandas.merge(studenti, jmena)
print(studentiPlusJmena)

# 7
import pandas
studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")
studenti = pandas.concat([studenti1, studenti2])
studenti = studenti.dropna()
jmena = pandas.read_csv("jmena.csv")



studentiPlusJmena = pandas.merge(studenti, jmena)
studentiPlusJmena.columns
print(  studentiPlusJmena.groupby("pohlaví").count() )
