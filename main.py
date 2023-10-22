# # # # ======= ARGUMENTS =======
# # # print("Hello", "World", "i", "am", "BACK😈") 


# # size = 10
# # for i in range(size):
# #     for j in range(size):
# #         if j 
# #         print("#", end="")
# #     print()


# # # LEFT-SIDED BINDING
# # name = 'nathan'
# # add = 2 + 3 + 4 + 5 - 6 # ANSWER = 8
# # # multiply = 2 * 3 + 6 * 4 # ANSWER = 48

# # exponent = 2 ** 3
# # left = exponent ** 4 

# # print(4 ** 3 ** 2, exponent)

# # largest_number = -99999999
# # number = int(input("Enter a number: "))
# # while number != -1:
# #     if number > largest_number:
# #         largest_number = number
# # print(largest_number)

# # name = input("Enter a name: ")

# # while name != 'nathan':
# #     print("INCORRECT!")
# #     name = input("Enter NATHAN !!! 🤦🏾‍♂️ ")
# # print('Hi, Nathan')

# # ====== WHILE STATEMENT ======
# import time

# # number = 10
# # while number >= 0:
# #     print(number)
# #     number -= 1
# #     time.sleep(1)
# #     if number == 0:
# #         print("BLAST OFF!🚀🚀")
# #         break

# # ====== FOR STATEMENT ======
# for i in range(10,-1,-1):
#     pass



# # ====== LIST AND TUPLES ======
# === ADDING ITEMS TO LIST === 

# 1. ============ INSERT METHOD ============
# -- Takes two arguments: The position and the item to be added
# -- Does not return anything.
print("ADDING ITEMS TO LIST\n")
my_list = [16, 2, 3]
print(my_list, "ORIGINAL")
for v in range(len(my_list)): # This will repeat 3 times (len(my_list))
    my_list.insert(1, my_list[v])
    print(my_list, "INSERTED")

print("======================")


# 2. ========== APPEND METHOD ============
# -- Adds an item at the end of the list
my_list = [16, 2, 3]
print(my_list, "ORIGINAL")
for v in range(len(my_list)): # This will repeat 3 times (len(my_list))
    my_list.append(my_list[v])
    print(my_list, "APPENDED")

print("======================")

# === REMOVING ITEMS FROM LIST === 
# 1. del keyword -- It DOES NOT return the deleted item from the list
print("DELETING ITEMS FROM LIST\n")
my_list = [16, 2, 3]

del my_list[0]
print(my_list, "Deleted first item")

# 2. Pop method -- It RETURNS the deleted item from the list
my_list = [16, 2, 3]
last_item = my_list.pop()
print(my_list, "Popped last item")
print(last_item, "is the last item that was popped")


print("==========================")

# METHODS IN LIST
# 1. sort Method - Arrange a list in ascending order
# --- USAGE: my_list.sort()

# 2. reverse Method - Reverses the current state of the list
# --- USAGE: my_list.reverse()

# ===========🔥 THE FOR VS THE LIST 🔥===========
print("BATTLE OF THE LOOPERS AND THE BUNKER (List)\n")

parent, child = 10, 4

my_list = [["4" for i in range(child)] for x in range(parent)]

print(len(my_list), "items are in the parent list")
print(len(my_list[0]), "items are in each sub-list")

print()
print("==========================\n")

t = [[3-i for i in range(3)] for j in range(3)]
# t = [[3,2,1], [3,2,1], [3,2,1]]
s = 0
print(t, "ORIGINAL LIST")
for i in range(3):
    s += t[i][i]
print(s)

