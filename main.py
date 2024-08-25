import random
choice = input("E for Encode , D for decode: ")

if choice.lower() ==  "e":

   # Encoding 
     user_input = input("Enter word to encode: ")
     wordtoencode = user_input.split()
     encodedword = []
     for words in wordtoencode:

       if len(words) >=3:
         alphabets_list= list('abcdefghijklmnopqrstuvwxyz')
         randomchars = random.sample(alphabets_list,k=26)
         randomstr = ''
         for chars in randomchars:
            randomstr+=chars

         newstr = randomstr[:3]+ words[1:] + words[0] + randomstr[3:6]
         encodedword.append(newstr)
       else:
          encodedword.append(words[::-1])
     print(" ".join(encodedword))

elif choice.lower() == "d":
     
    # Decoding
    user_input = input("Enter word to decode: ")
    wordtodecode = user_input.split()
    decodedword = []
    for words in wordtodecode:
      if len(words) >=3:
       newstr = words[3:-3] 
       newstr = newstr[-1] + newstr[:-1]

       decodedword.append(newstr)

      else:
        decodedword.append(words[::-1])

    print(" ".join(decodedword))
else:
    print("Invalid Input!")
