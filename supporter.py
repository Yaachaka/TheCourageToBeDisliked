arr1 = []

with open("supporter.txt", "r") as file1:
	for line in file1:
		arr1.append(line)

chapter_x = "chapter_03p13"

# print("\t<hr class=\"contentDivide\">")
# print("\t<div class=\"chapter_03\" id=\"id-chapter_03\">")
arr1_len = len(arr1)
for i in range(arr1_len):
	pos = arr1[i].index(": ")
	var1 = arr1[i][pos+2:-1]
	if "HEADER2: " in arr1[i]:
		print("\t<h2>" + var1 + "</h2>")
	elif "HEADER3: " in arr1[i]:
		# print("\t</div>")
		print("\t<hr class=\"contentDivide\">")
		print("\t<div class=\"{}\" id=\"id-{}\">".format(chapter_x, chapter_x))
		print("\t\t<h3>" + var1 + "</h3>")
	elif "NARRATOR: " in arr1[i]:
		print("\t\t<div class=\"narrator\">")
		print("\t\t\t<p>" + var1 + "</p>")
		print("\t\t</div>")	 
	elif "YOUTH: " in arr1[i]:
		print("\t\t<div class=\"youth\">")
		print("\t\t\t<p>" + var1 + "</p>")
		print("\t\t\t<img src=\"./images/youth.png\" alt="">")
		print("\t\t</div>")	 
	elif "PHILOSOPHER: " in arr1[i]:
		print("\t\t<div class=\"philosopher\">")
		print("\t\t\t<img src=\"./images/philosopher.png\" alt="">")
		print("\t\t\t<p>" + var1 + "</p>")
		print("\t\t</div>")
print("\t</div>  <!-- End of {} -->".format(chapter_x))