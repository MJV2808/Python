# students in exams
cet = {"Alice", "Bob"}
jee = {"Bob", "Eve"}
neet = {"Alice", "Eve"}
print("All students:", cet|jee|neet) #Union
print("Students in all exam:", cet & jee & neet) # intersection
print("Cet but not in jee:", cet - jee) #Difference
