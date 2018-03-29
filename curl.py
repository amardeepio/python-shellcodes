import sh as bada 

x =bada.curl("http://ndtv.com","-v" )
print x 

print ("the number of files in my currenyt directory  is : \n")

#print ( bada.wc(bada.find("/home/amardeep/"),  "-l"))

print (bada.grep(bada.dmidecode(),"AMD"))

print("printing my current processor and memory information: \n")

print (bada.tail(bada.head("-n",130,"dmi.txt"),"-n",20))

print "getting current directory \n" , bada.pwd()


