# User input নেওয়া এবং integer-এ কনভার্ট করা
user = int(input("Enter your exam result: "))

# Function তৈরি করা
def re(marks):
    if marks >= 90:
        print("Awesome! You did a great job!")
    elif marks >= 80:
        print("Good job! You did well!")
    elif marks >= 70:
        print("Good! A little more attention would be great.")
    elif marks >= 60:
        print("You need to work harder.")
    elif marks >= 50:
        print("You have to try harder.")
    else:
        print("You need a lot more effort!")

# Function কল করা
re(user)