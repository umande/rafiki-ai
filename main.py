# from Rafiki_Brain.rafikiBrain import brain
import re

# brain.speak("welcome ")
# brain.main()
def check(string):
    reg = re.compile("go+\w*")
    mach_object = reg.findall(string)
    if len(mach_object) !=0 :
        for word in mach_object:
            print(word)
    else:
        print("no match")

word = input("enter : ")
check(word)



