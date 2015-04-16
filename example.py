import kdapi

# get just similar images
for item in kdapi.check("http://imgur.com/ndDmnN4"):
    print(item.title + "(" + str(item.time) + ") : " + item.link)

# get simliar and less similar images
similar, lessSimilar = kdapi.check("http://imgur.com/ndDmnN4",True)
for item in lessSimilar:
    print(item.title + "(" + str(item.time) + ") : " + item.link)
