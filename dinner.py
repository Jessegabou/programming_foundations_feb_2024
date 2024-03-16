name = ""
entree = ""
side_one = ""
side_two = ""
dessert_one = ""
dessert_two = ""
dessert_three = ""

#Step 1: Ask for a name
name = input("What is your name?: ")

#Step 2: Ask for the entree (main course)
entree = input("What is your entree?: ")

#Step 3: Ask for first side
side_one = input("What is your first side?: ")

#Step 4: Ask for second side
side_two = input("What is your second side?: ")

#Step 5: Ask for the first desert
dessert_one = input("What is your first dessert?: ")

#Step 6: Ask for the second desert
dessert_two = input("What is your second desert?: ")

#Step 7: Ask for the third desert
dessert_three = input("What is your third desert?: ")

# process
dinner_decisions = f"""
Hi, my name is {name}.
I chose {entree} as my main meal!
To go with it, I chose {side_one} and {side_two} as my sides.
And the best part, I have {dessert_one}, {dessert_two}, and {dessert_three} waiting for me dessert!
Let's eat!
"""

#output
print(dinner_decisions)