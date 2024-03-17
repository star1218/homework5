# import shutil #1
# with open("wello1.txt", 'w') as my_file:
#     my_file.write("hobby horsink")
#
# with open("wello2.txt","w") as number_file:
#     shutil.copyfile("wello1.txt","wello2.txt")


# with open("hello1.txt", "w", encoding="utf-8") as my_file: #1
#     my_file.write("Привет Петя ")
#
# with open("hello1.txt", "r", encoding="utf-8") as my_file:
#     result = my_file.read()
#
# with open("hello2.txt", "w", encoding="utf-8") as number_file:
#     number_file.write(result)
#
# with open("hello1.txt","w",encoding="utf-8") as my_file: #2
#     my_file.write("Привет, дорогой друг")
#
# with open("hello1.txt","r",encoding="utf-8") as my_file:
#     result = my_file.read()
#     words = result.split()
#     words_count=len(words)
# print("В файле всего слов:",words_count)