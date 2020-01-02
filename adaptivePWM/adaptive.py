count = [0,0,0,0]
flag = [False,False,False,False]
vals = [[0 for i in range(4)] for i in range(1000)]
temp_pwm = [50,50,50,50]
pwm = [50,50,50,50]
prev = [0,0,0,0]
KP = 3

for i in range(4):
  flag[i]=False
  count[i]=0

for i in range(1000):
  for j in range(4):
    vals[i][j]=0  #digitalRead(pins[j])
  
for i in range(1000):
  for j in range(4):
    if not vals[i][j] == flag[j]:
      if vals[i][j] == True:
        flag[j] = True
        count[j] += 1
      else:
         flag[j] = False
 
for i in range(4):
  prev[i] = temp_pwm[i] - pwm[i]

for i in range(4):
  factor = (count[i] -40)/KP
  temp_pwm[i] = pwm[i] - factor + prev[i]
  print factor,"-",prev[i],"-",temp_pwm[i]
print ""

# analogWrite(m11, temp_pwm[0]);
# analogWrite(m21, temp_pwm[1]);
# analogWrite(m31, temp_pwm[2]);
# analogWrite(m41, temp_pwm[3]);