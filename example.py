import kdapi

for item in kdapi.check("http://imgur.com/ndDmnN4"):
    print(item.title + "(" + str(item.time) + ") : " + item.link)
