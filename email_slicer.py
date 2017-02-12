email = input("Enter your email addresss?: ").strip()
domain = email[email.index("@")+1:]
username = email[:email.index("@")]
print(email)
print(username)
print(domain)
output = "your username is {} and your domain is {}".format(username,domain)

print(output)
