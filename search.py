import json
from difflib import get_close_matches

data = json.load(open("db.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        ans = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if ans == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif ans == "N":
            return "The term does not exist."
        else:
            return "We didn't understand your entery."
    else:
        return "The term does not exist."


term = input("enter term: ")

output = translate(term)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
