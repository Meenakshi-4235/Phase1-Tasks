subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]

sentences = []

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{subject} {verb} {obj}."
            sentences.append(sentence)

# Printing all generated sentences
for sentence in sentences:
    print(sentence)
