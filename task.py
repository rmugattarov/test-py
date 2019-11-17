lines = open('input.txt').readlines()
n = int(lines[0])
allVotes = [0] * 32767
for i in range(1, n + 1):
    split = lines[i].split(' ')
    start = int(split[0])
    end = int(split[1])
    votes = int(split[2]) + 1
    for j in range(start, end + 1):
        allVotes[j] = allVotes[j] + votes
maxVotes = 0
for i in allVotes:
    maxVotes = max(maxVotes, i)
print(maxVotes)
