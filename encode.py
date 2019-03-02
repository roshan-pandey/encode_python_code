a = "aaaabbccc#"
encoded_string = ""
point = -1
i = 0
while i < len(a):
    counter = 1
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            counter += 1
        else:
            encoded_string += str(counter)
            encoded_string += a[i]
            i += counter
            break
    if i == len(a)-1:
        break

print(encoded_string)
