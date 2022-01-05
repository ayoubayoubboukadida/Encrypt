print ("<---------------------------------------------------------------->")
print ("1) Encrypt")
print ("2) decrypt")
print ("<---------------------------------------------------------------->")
print("")



a =input("Choose a number -->")
if a =="1":
    def encryption_text(text):
        x="abcdefghijklmnopqrstuvwxyz "
        y="12345678900987654321012345"
        enc_text=""
        for char in text :
            index=x.index(char)
            enc_text+=y[index]
        return enc_text
    text=encryption_text(input("Type something for encryption -->"))
    print("Encryption has been made:  "+text)
else:
    print("No")
