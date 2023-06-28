string = "I am learning to code"
ans = ""
for i in range(0, len(string)):
    if i % 2 == 0:
        ans += string[i].upper()
    else:
        ans += string[i]
print(ans)

words = string.split(" ")
for i in range(0, len(words)):
    if i % 2 != 0:
        words[i] = words[i].upper()
    else:
        words[i] = words[i].lower()
print(" ".join(words))
