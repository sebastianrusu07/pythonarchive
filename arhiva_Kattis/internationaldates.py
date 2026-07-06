date = input()

month = int(date[3:5])
days=int(date[:2])
guess = "either"
if month>12 :
    guess = "US"
elif days>12 :
    guess = "EU"

print(guess)


