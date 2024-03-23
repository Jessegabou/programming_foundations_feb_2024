import csv

with open('dinner.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)

        for row in csvreader:
            print(row)
            # process
            dinner_decisions = f"""
            Hi, my name is {row[0]}.
            I chose {row[1]} as my main meal!
            To go with it, I chose {row[2]} and {row[4]} as my sides.
            And the best part, I have {row[4]}, {row[5]}, and {row[6
            
            ]} waiting for me dessert!
            Let's eat!
            """

            #output
            print(dinner_decisions)