print("Your family runs a cookie factory.")
cookie_num = input("How many cookies did you make today? ")
cookie_num = int(cookie_num)
cookies_per_box = input("How many cookies are in each box? ")
cookies_per_box = int(cookies_per_box)
boxes = cookie_num // cookies_per_box
leftover_cookies = cookie_num % cookies_per_box
print(f"You made {boxes} boxes of cookies.")
print(f"You have to eat {leftover_cookies} leftover cookies!")
