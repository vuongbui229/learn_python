# list (Mảng)
# my_cart = []
# my_cart = list()

# my_cart.append("Cam")
# my_cart.append("Chuối")
from pickle import TRUE


my_family = ['bố', 'mẹ', 'con trai', "bà", "bà"]

# for loop
for i in my_family:
    print(i)

print("bà" not in my_family)
new_member = "bà"
if new_member not in my_family:
    my_family.append(new_member)


cart_1 = ["orange", "apple", 1, 2, ["bo", "me"]]
cart_2 = ["banana", "grape", "lemon"]
cart_1.extend(cart_2)
print(my_family)
print(my_family.count("bà"))

tmp_list = my_family.copy()

tmp_list.append("ông")

print("my_family: ", my_family)
print("tmp_list: ", tmp_list)

my_nums = [1, 2, 3]

my_nums.insert(1, 10)
print(my_nums)


# my_nums.reverse()
my_nums.sort(reverse=True)
print(my_nums)
print(my_family.index("bà"))