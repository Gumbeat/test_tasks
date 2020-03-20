from urllib.request import urlopen

data = urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().decode("utf-8").split()
data_dict = {}
for word in data:
    sw = str(sorted(word))
    if sw not in data_dict:
        data_dict[sw] = []
    data_dict[sw].append(word)
for value in data_dict.values():
    if len(value) > 1:
        print(*value)
