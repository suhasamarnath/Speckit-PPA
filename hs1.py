students = {"Alex" : {"Math" : "50", "Physic" : "98", "Chemistry" : "69", "Biology" : "78", "Social-Science" : "89" },
"Steve" : {"Math" : "78", "Physic" : "87", "Chemistry" : "98", "Biology" : "88", "Social-Science" : "79"},
"Martin" : {"Math" : "45", "Physic" : "99", "Chemistry" : "100", "Biology" : "89", "Social-Science" : "88"},
"Trish" : {"Math" : "66", "Physic" : "68", "Chemistry" : "70", "Biology" : "71", "Social-Science" : "68"}}
details = {"Trish" : "Math", "Alex" : "Chemistry", "Martin" : "Biology"}

for name in details:
	output = students[name][details[name]]
	print(name, "scored", output, "in", details[name])