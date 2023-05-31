import os

os.system("cls")
# emoji mapping
message = input("[>] : ")

emoji_mapping = {
  ":)":"😊",
  ":D":"😁",
  ":*":"😘",
  ":p":"😋",
  "8)":"😎"
}

words = message.split(" ")

output = ""
for w in words:
  output = output + emoji_mapping.get(w, w) + " "
print(output)