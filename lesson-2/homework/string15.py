sent = input("Enter a sentence: ")
sent_list = sent.split()
acronym = "".join(word[0] for word in sent_list)
print(acronym)
