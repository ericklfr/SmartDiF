with open("urls.txt", "r+") as f:
    old = f.read() # read everything in the file
    f.seek(0) # rewind
    f.write(old+"\nurl(r'^$', views.home, name='home'),")
    print(f.readlines())