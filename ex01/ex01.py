from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    d = defaultdict(list)
    for s in strs:
        l = list(s)
        l.sort()
        d["".join(l)].append(s)
    res = []
    for l in d.values():
        res.append(l)
    return res

# if __name__ == "__main__":
#     # strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
#     # strs = ['']
#     strs = ['a']
#     print(group_anagrams(strs))