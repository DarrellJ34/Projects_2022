# Program that allows an unlimited amount of numeric data entries and finds the average of them

data_points = []

data_points.append(float(input("Enter your first number: ")))
data_points.append(float(input("Enter your second number: ")))
more = input("Do you have more numbers?: ").capitalize()
if more == "No":
    print(sum(data_points) / len(data_points))
elif more == "Yes":
    data_points.append(float(input("Enter your next number: ")))
    print(sum(data_points) / len(data_points))
    more = input("Do you have more numbers? Yes or No: ").capitalize()
    while more == "Yes":
        data_points.append(float(input("Enter your next number: ")))
        print(sum(data_points) / len(data_points))
        more = input("Do you have more numbers? Yes or No: ").capitalize()