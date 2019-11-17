import sys
print('Hello!')
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
for l in open('data.txt'):
    print(int(l))
