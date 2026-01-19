l = list("first")
print(l)

print("--------")

import math
print(math.pi)
print(round(13.53287, 2))

print('"Hello \"\"\"\'\' \n World"')
print("-------")
s = "Hello, \nworld!"
print(s)

s = "Hello, \\n world!"
print(s)

s = r"Hello, \n world!"
print(s)

s = r"Hello, \n'''' world!"
print(s)

email = "user@domain.com"
print(email[0])

print(email[-1])

print(email[0:5])

print(email[0:10:2])

assert email.endswith("@domain.com")
print(email.split("@"))

print(email.
      split("@"))

a = "Hello"
b = "world"

print(a + b)
print(a + ", " + b + "!")

print("{a}, {b}!".format(a=a, b=b))
print(f"{a}, {b.upper()}!")
print(f"{a=}, {b=}!")
print("%s, %s!" % (a, b))

url_template = "https://www.yourservice.com"

user_url = url_template.format("users")
groups_url = url_template.format("groups")

s = "1234"
n = 1234
# assert int(s) == n

assert s.isdigit()

#списки

l = [1, 2, 3, a, b, [4, 5, 6]]
print(l[0])
print(l[-1][1])
print(l[::-1])


l.append(7)
l.extend(["elem", "another elem"])
l.reverse()
l.reverse()
print(len(l))
print(l)

l[0] = 200

print(l)








