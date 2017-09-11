import os




os.chdir('C:\\Users\\User')

print(os.path.split('C:\\Users\\User'))
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
k = os.getcwd()
print(k)
os.chdir(k + '\\' + 'User')
print(os.getcwd())



