"""
    Problem: 966. Vowel Spellchecker
    Link: https://leetcode.com/problems/vowel-spellchecker/

    Description:
        Implement a spellchecker that matches queries to given wordlist
        according to these rules:
        1. Exact match first.
        2. Case-insensitive match.
        3. Vowel-error match (treat all vowels as interchangeable).
        Return the corrected word from wordlist or empty string if no match.

    Approach:
        - Preprocess wordlist into hashmaps for fast lookup.
        - Check queries against maps in priority order.
    
    Time: O(N * M) where N is the length of queries and M is the average length of words in wordlist
    Space: O(W) where W is the number of unique words in wordlist
    """
def spellchecker(wordlist, queries):
    exact_map = {word for word in wordlist}
    case_map = {}
    crypted_map = {}
    for word in wordlist:
        lw = word.lower()
        if lw not in case_map:
            case_map[lw] = word
        dv = devowel(lw)
        if dv not in crypted_map:
            crypted_map[dv] = word

    result = []
    for w in queries:
        crypted_word = devowel(w)
        w_lower = w.lower()
        if w in exact_map:
            result.append(w)
        elif w_lower in case_map:
            result.append(case_map[w_lower])
        elif crypted_word in crypted_map:
            result.append(crypted_map[crypted_word])
        else:
            result.append("")

    return result

def devowel(word: str) -> str:
    vowels = set("aeiou")
    return "".join("*" if ch in vowels else ch for ch in word.lower())



# Examples
print(spellchecker(
    ["KiTe","kite","hare","Hare"],
    ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
))
# Expected: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

print(spellchecker(
    ["yellow"],
    ["YellOw","yollow","yllw","YELLOW"]
))
# Expected: ["yellow","yellow","","yellow"]

print(spellchecker(
    ["a","b"],
    ["A","e","B","z"]
))
# Expected: ["a","","b",""]