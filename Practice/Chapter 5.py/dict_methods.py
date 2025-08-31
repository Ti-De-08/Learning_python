marks = {"Harry" : 45,
"Tom" : 30,
"Jerry" : 35,
20 : "Gordon"
} 


print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Tom" :40, "Ross" : 50})
print(marks)
print(marks.get("Tom"))
print(marks.get("Tim")) #returs None
print(marks["Tim"]) #throws error