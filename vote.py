vote = {}
person = input("Enter a Musician (Type done when done voting): ")

while person != "done":
    fix_name = person.title()
    if fix_name in vote:
        vote[fix_name] += 1
    else:
        vote[fix_name] = 1
    person = input("Enter a Musician (Type done when done voting): ")
    if person == "done":
        break
print("Votes:")
print("----------")
for musician, votes in sorted(vote.items()):
    print(f"{musician}: {votes}")