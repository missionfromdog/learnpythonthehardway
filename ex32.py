the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    #variable named number is assigned the value of each element
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    #variable named fruit is assigned each value of the element fruits
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    #variable named i is assigned each value of the element change
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range (0,6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

print(">>>> after range: i=", i)

#now we can print them out too
for i in elements:
    print(f"Elements was: {i}")
