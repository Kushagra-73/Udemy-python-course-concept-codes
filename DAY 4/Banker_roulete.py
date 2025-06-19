# Figure out how to pick a random name from the list of friends.

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
ran_frd=random.randint(0,4)

# 1st option
# print(f"{friends[ran_frd]} will paying thois today's bill ")

# OR 
# 2nd option = random.choice()
print(random.choice(friends))


