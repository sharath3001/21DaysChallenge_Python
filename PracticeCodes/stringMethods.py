print('aBcD'.capitalize())
print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')
print("epsilon".endswith("on"))
print("Eta".find("ta"))
print("Eta".find("mma"))
print('kappa'.find('a', 2))
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print("Moooo".isalpha())
print('Mu40'.isalpha())
print('2018'.isdigit())
print("Year2019".isdigit())
print("Moooo".islower())
print('moooo'.islower())
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
print(",".join(["omicron", "pi", "rho"]))
print("SiGmA=60".lower())
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
print("tau tau tau".rfind("ta")) # r is for right
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
print("phi       chi\npsi".split())
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()
print("[" + "   aleph   ".strip() + "]")
print("I know that I know nothing.".swapcase())
print()
print("I know that I know nothing. Part 1.".title())
print()
print("I know that I know nothing. Part 2.".upper())
