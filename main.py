import single_line
from init import init
def main(filename,r):
	interpreted = False
	with open(filename,r) as f:
		lines=r.readlines()
    	init(f,filename)
    	interpreted = True
    	for line in lines:
      		if str(filter(lambda x:not (x == ' '),line))[0] = "#":
        		continue
      		else:
        		single_line.interpret(line)
	if not interpreted:
    		print(f"The file {filename} doesnt exist")
