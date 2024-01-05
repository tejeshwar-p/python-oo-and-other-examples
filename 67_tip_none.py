# None is kind of like null. It is used to denote there is no value
# Using None is considered good practice
print(type(None))


def email(subject, content, to, cc=None, bcc=None):
    print(f"{subject}, {content}, {to}, {cc}, {bcc}")


email("subject", "great work", "someemail@email.com")
email("subject", "great work", "someemail@email.com", None, None)

some_var = "123"
if some_var is None:
    print("perform something")

some_var = None
if some_var is None:
    print("perform something else")

