print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word:")

if len(original) > 0 and original.isalph():
    print(original)
else:
    print("empty")
