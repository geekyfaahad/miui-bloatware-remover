import os
p = open("bloat.txt", "r")
for x in p:
    print(x)
    os.system("adb devices")
    os.system(f"adb shell pm uninstall --user 0 {x}")
