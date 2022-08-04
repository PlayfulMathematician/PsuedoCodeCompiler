import single_line
def main(filename,r):
  with open(filename,r) as f:
    lines=r.readlines()
    for line in lines:
      if str(filter(lambda x:not (x == ' '),line))[0] = "#":
        continue
      else:
        single_line.interpret(line)
      
