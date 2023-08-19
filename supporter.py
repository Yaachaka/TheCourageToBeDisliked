arr1 = []

with open("supporter.txt", "r") as file1:
	for line in file1:
		arr1.append(line)

print("<div class=\"chapter_02\" id=\"id-chapter_02\">")
arr1_len = len(arr1)
for i in range(arr1_len):
	pos = arr1[i].index(": ")
	var1 = arr1[i][pos+2:-1]
	if "HEADER2: " in arr1[i]:
		print("\t<h2>" + var1 + "</h2>")
	elif "HEADER3: " in arr1[i]:
		print("\t<h3>" + var1 + "</h3>")
	elif "NARRATOR: " in arr1[i]:
		print("\t<div class=\"narrator\">")
		print("\t\t<p>" + var1 + "</p>")
		print("\t</div>")	 
	elif "YOUTH: " in arr1[i]:
		print("\t<div class=\"youth\">")
		print("\t\t<p>" + var1 + "</p>")
		print("\t\t<img src=\"./images/youth.png\" alt="">")
		print("\t</div>")	 
	elif "PHILOSOPHER: " in arr1[i]:
		print("\t<div class=\"philosopher\">")
		print("\t\t<img src=\"./images/philosopher.png\" alt="">")
		print("\t\t<p>" + var1 + "</p>")
		print("\t</div>")
print("</div>")
print("<hr class=\"contentDivide\">")