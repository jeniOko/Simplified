#emoji dictionary
message= input("> ")
words = message.split(" ")#will split words by space and create a list
emojis = {
    ":)": "🙂",
    ":(": "😔",
    ":D": "😃",
    ":*": "😘",
    ":'(": "😪",
    ":/": "😏",
    "O:)": "😇",
    ":P": "🤪",
    ":O": "😧",
    "^_^": "😊",
    ">:O": "😆",
    ">:(": "😣",
    "8|": "😎",
    "-_-": "😑",
    "<3": "❤"
}

output = ""
for word in words:
    output += emojis.get(word,word) +" "
print(output)
