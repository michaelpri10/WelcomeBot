def check_user(user):
  new = true
  try:
    f = open("users.txt", "r")
    try:
      file = f.readlines()
    finally:
      f.close()
  except IOError:
    pass
    
  for x in len(file):
  	if user == file[x]:
      new=false
    
  if new==true:
    try:
	  logfile = open("users.txt", "a")
	  try:
	    logfile.write(user)
	  finally:
	    logfile.close()
	  except IOError:
	    pass
return new
