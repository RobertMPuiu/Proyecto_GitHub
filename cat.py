import sys

if len(sys.argv) != 2:
  sys.stderr.write('to run with one arguments\n')
  exit()
try:
  fh = open(sys.argv[1],"r")
except FileNotFoundError:
  sys.stderr.write(sys.argv[1] + ' not exists \n')
  exit()
fe = open("upper","w")
fi = open("lower", "w")
line = fh.readline().strip()
while line:
  if line.isupper():
   fe.write(line + '\n')
  if line.isnumeric():
   print("Número: " + str(line))
  if line.islower():
   fi.write(line + '\n')
  line = fh.readline().strip() 

fh.close()
fe.close()
fi.close()
