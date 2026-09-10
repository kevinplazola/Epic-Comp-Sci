Classifier = input("Classifier: ")
def classified():
    target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
    global Classifier
    words = Classifier.split(" ")
    for w in words:
        if w.lower() in target_words:
         Classifier = Classifier.replace(w, "[REDACTED]")
    return Classifier
    
print(classified())