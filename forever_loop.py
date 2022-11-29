counter = 0
while True :
  print ("Never going to ____ up")
  print ()
  ans = input ("Let's see if you are as smart as me,\nwhat would your ans for this question???  ")
  if ans == 'give' :
    print ('Yeah, you got the right ans!!!')
    break
  else :
    print ('Sorry 😢😢😢, try again!')
    counter += 1 

print("You got the correct lyrics in", counter, "attempt(s).")