# import shutil #1 не то задание
# with open("wello1.txt", 'w') as my_file:
#     my_file.write("hobby horsink")
#
# with open("wello2.txt","w") as number_file:
#     shutil.copyfile("wello1.txt","wello2.txt")


# with open("hello1.txt", "w", encoding="utf-8") as my_file: #1 не то задание
#     my_file.write("Привет Петя ")
#
# with open("hello1.txt", "r", encoding="utf-8") as my_file:
#     result = my_file.read()
#
# with open("hello2.txt", "w", encoding="utf-8") as number_file:
#     number_file.write(result)
#

# with open("hello1.txt", "w", encoding="utf-8") as ferst_file: #1 готовое
#     ferst_file.write("Быть или не быть, вот в чем вопрос: благороднее ли в уме страдать от пращ и стрел возмутительной фортуны")
#
#
# with open("hello1.txt", "r", encoding="utf-8") as my_file:
#     content = my_file.read().split()
#     filtered_words = [word for word in content if len(word) >= 7]
#
# with open("hello2.txt", "w", encoding="utf-8") as number_file:
#     number_file.write(" ".join(filtered_words))


# with open("hello1.txt","w",encoding="utf-8") as my_file: #2 готовое
#     my_file.write("Быть или не быть, вот в чем вопрос: благороднее ли в уме страдать от пращ и стрел возмутительной фортуны")
#
# with open("hello1.txt","r",encoding="utf-8") as my_file:
#     result = my_file.read()
#     words = result.split()
#     words_count=len(words)
# print("В файле всего слов:",words_count)


# def replace_word(text, word, replacement): #3 готовое
#     return text.replace(word, replacement)
#
#
# def main():
#     text = """To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer
#     The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles,
#     And by opposing end them? To die: to sleep; No more; and by a sleep to say we end
#     The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation
#     Devoutly to be wish'd. To die, to sleep."""
#     word_replace = "die"
#     replaced_text = replace_word(text, word_replace, "*" * len(word_replace))
#     print("Измененый текст")
#     print(replaced_text)
#
#
# if __name__ == "__main__":
#     main()
