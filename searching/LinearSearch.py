array=[23,56,45,76,87,24,48]
ele=45
for i in range(len(array)):
    if array[i]==ele:
        print("Element found at position ",i)
        exit()
print("Element not found")