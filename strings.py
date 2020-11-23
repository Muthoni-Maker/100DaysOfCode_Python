#Day21-30#
#Quiz1: Write a Python program to calculate the length of a string#
string="Hello Kenya"
length_of_the_string=len(string)
print(length_of_the_string)

#Quiz2:Write a Python program to count the number of characters (character frequency) in a string.#
def character_count(word):
  dict={}
  for i in word:
    keys=dict.keys()
    if i in keys:
      dict[i]+=1
    
    else:
      dict[i]=1

  return(dict)

x=character_count("I love reading science fiction novels every morning especially when I feel low since they tend to boost my imagination and thinking capacity.")

print(x)

#Quiz3: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string#


  
