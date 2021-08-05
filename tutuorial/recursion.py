def cleanWord(word):

  if len(word) == 1:

    return word

  print(f"Print Start Function {word}")

  if word[0] == word[1]:

    print(f"Print Before Condition {word}")

    return cleanWord(word[1:])

  print(f"Print Before Return {word}")
  print(word[0])
  result=word[0] + cleanWord(word[1:])
  

  return result

  # Stash [ World ]

print(cleanWord("WWWoooorrrldd"))