# Email Slicer
# Input: john12@hotmail.com
# Output: The username is John12 and domain is hotmail.com

email = input("Enter your email:").strip() #strip is used to remove the white spaces from starting and from the end.
username = email[:email.index('@')]
domain = email[email.index("@") + 1 :]

print("The username is",username,"and domain is",domain)

#Domain Name from a Hyperlink
#Using strip()

hyperlink = ("https://google.com").strip("https://")
print(hyperlink)

#using urlparse
import urllib.parse

domain = urllib.parse.urlparse("https://www.example.com/page.html")
print(domain)
print(domain.netloc)