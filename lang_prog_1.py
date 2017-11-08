import re

def same(ip1,ip2):
	if ip1.split(".")[0] == ip2.split(".")[0]:
		if ip1.split(".")[1] == ip2.split(".")[1]:
			if ip1.split(".")[2] == ip2.split(".")[2]:
				return True
	return False

def full_same(ip1,ip2):
	if ip1.split(".")[0] == ip2.split(".")[0]:
		if ip1.split(".")[1] == ip2.split(".")[1]:
			if ip1.split(".")[2] == ip2.split(".")[2]:
				if ip1.split(".")[3] == ip2.split(".")[3]:
					return True
	return False


file = open("access.log","r")
data = file.read()
file.close()
regex = "[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}"
mas_ip = re.findall(regex,data)

mas_res = []
x = False;
for i in range(len(mas_ip)):
	for j in range(len(mas_res)):
		if same(mas_ip[i], mas_res[j][0]) == True:
			x = True
			continue
	if x == True:
		x = False
		continue
	else:
		mas_res.append([mas_ip[i]])

z = False
for i in range(len(mas_ip)):
	for j in range(len(mas_res)):
		z = same(mas_ip[i],mas_res[j][0])
		if z == True:
			for k in range(len(mas_res[j])):
				if full_same(mas_ip[i],mas_res[j][k]) == False:
					if len(mas_res[j])-k == 1:
						mas_res[j].append(mas_ip[i])
					continue
				else:
					break
			break
	if z == False:
		mas_res.append([mas_ip[i]])
	z = False

file = open("result.txt","w")
for i in range(len(mas_res)):
	for j in range(len(mas_res[i])):
		file.write(mas_res[i][j] + "   <----->   ")
	file.write("\n")
file.close()