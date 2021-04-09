#RyanWaltersDev Apr19 -- Using a not in keyword to check for banned users Ch5

banned_users = ['xXxLegolas_DarkAngelxXx', 'Urmom', 'Fartmaster9000']
user = "GabeN_Official"

if user not in banned_users:
    print(f"{user}, we are working on posting your comment now!")
else:
    print("You are banned! Begone vile man! Begone from me!")

#END OF PROGRAM
