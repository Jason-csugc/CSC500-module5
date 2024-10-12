

num_books_purchased = int(input("Enter the number of books purchased: "))

points_earned = 0

if num_books_purchased >= 2 and num_books_purchased < 4:
    points_earned = 5
elif num_books_purchased >= 4 and num_books_purchased < 6:
    points_earned = 15
elif num_books_purchased >=6 and num_books_purchased < 8:
    points_earned = 30
elif num_books_purchased >= 8:
    points_earned = 60
else:
    points_earned = 0
10
print(f"{points_earned} Points Earned")