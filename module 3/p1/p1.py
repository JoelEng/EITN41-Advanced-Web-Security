key_og = open("key.pem", "r")
key = open("clean_key.pem", "w")
print(key.write(key_og.read().replace("censored", "")))
