

b=open('demo.txt','a')
b.write('hello world')
b.close()


a=open('demo.txt','r')
print(a.read())
a.close()

a=open('demo.txt','r')
print(a.readline())

text = a.read()
words = text.split()
print("Word count:", len(words))

a.close()






