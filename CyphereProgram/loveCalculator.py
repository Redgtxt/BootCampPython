import string
def calculate_love_score(name1,name2):
    count_true = 0
    count_love = 0
    names = []
    names.append(name1)
    names.append(name2)
    for word in names:
        for c in word:
            if(c in "true"):
                count_true += 1
            if(c in "love"):
                count_love += 1
    print(f"{count_true}{count_love}")
    
    
calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")
