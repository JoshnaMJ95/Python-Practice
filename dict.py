Dictionary_Name = dict()
print(Dictionary_Name)
print(type(Dictionary_Name))
phone_book= {
    'ramu':'1234',
    'jin':'345',
    'v':'7'
    }
print("phone number:",phone_book['ramu'])
print("phone number:",phone_book['jin'])
phone_book=dict(
    ramu='1234',
    jin='345',
    v='7'
    )
print("phone number:",phone_book['ramu'])
print("phone number:",phone_book['jin'])
words = {}
words["hello"] = "Bonjour"
words["yes"] = "oui"
words["no"] = "non"
print(words)
for key in words:
        print(key,"is:",words[key])
