count = 0
flag = False
vals = [0 for i in range(1000)]
temp_pwm = 50
pwm = 50
prev = 0
KP = 3

flag=False
count=0

for i in range(1000):
  vals[i]=0  #digitalRead(pins[j])
  
for i in range(1000):
  if not vals[i] == flag:
    if vals[i] == True:
      flag = True
      count += 1
    else:
        flag = False
 
prev = temp_pwm - pwm

factor = (count -40)/KP
temp_pwm = pwm - factor + prev
print factor,"-",prev,"-",temp_pwm

# analogWrite(m11, temp_pwm[0]);