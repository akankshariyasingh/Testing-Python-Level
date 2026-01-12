'''

loops_problem_1.5 - Given a string , performs the following using only loops and conditions:

1. Count total characters
2. Count vowels
3. Count consonants
4. Count digit
5. Count spaces 
6. Reverse the string 
7. Check if the string is a palindrome(ignoring spaces)
8. Print frequency of each character(order preserved)

'''

text= " coding is a therapy 12321 "
word=text.split()
vowels=("aeiouAEIOU")
total_ch_count=0
vowel_count=0
consonants_count=0
digit_count=0
space_count=0
reverse_text=""
for word in text:
        total_ch_count+=1
        reverse_text=word+reverse_text

        if word==" ":
            space_count+=1
        elif word in vowels:
            vowel_count+=1
        elif word>='0' and word<='9':
            digit_count+=1
        else:
             consonants_count+=1

print(total_ch_count)
print(space_count)
print(vowel_count)
print(consonants_count)
print(digit_count)
print(space_count)
print(reverse_text)

clean_text=""
for word in text:
     if word != ' ':
          clean_text+=word
reverse_clean=""
for word in clean_text:
    reverse_text= word+reverse_text
    if clean_text==reverse_text:
        print("Palindrome:Yes")
    else:
        print("Palindrome:No")

print("\n character Frequency:")
for i in range(len(text)):
    count=0
    for j in range(len(text)):
        if text[i] not in reverse_text:
            count=0
            for j in range(len(text)):
                if text[i]==text[j]:
                    count+=1
                reverse_text+=text[i]

                if text[i]==" ":
                    print("(space)->", count)
                else:
                    print(text[i], "->", count)       
           
     

     


                     
        
    


