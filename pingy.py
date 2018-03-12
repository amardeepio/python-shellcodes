import subprocess 

host = raw_input("enter a host to find its ip: ")
host1=raw_input("enter a web address to find its stats: ")

p1=subprocess.Popen(['nslookup',host],stdout=subprocess.PIPE)
p2=subprocess.Popen(['whois',host1],stdout=subprocess.PIPE)
p3=subprocess.call(["ls","-l","/home/amardeep"])

output1=p1.communicate()[0]
output2=p2.communicate()[0]


print(output1)
print(output2)