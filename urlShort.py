import pyshorteners

print ("Hello welcome to url shortener!")
link = input("Enter the link: ")
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)
print ("Your shortened url: ", x)
