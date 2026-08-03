
name = 'Danny' # input('name?')
print(type(name))

################# len
print('length of Danny is', len(name))
print(f'length of Danny is {len(name)} characters')

################## upper lower
name = 'danny'
print(str.upper(name))  # DANNY
print(name.upper())  # DANNY

yossi = 'YOSI'
print(yossi.lower())  # yossi

################# switch between text old -> new
sentence = "Hello, World!!"
print(sentence.replace("World", "Universe"))  #  "Hello, Universe!!"
print(str.replace(sentence, "World", "Universe"))  #  "Hello, Universe!!"

################# make list of words with specific seperator
sentence: str = "Hello, World!! good morning"
print(f"'{sentence}'", sentence.split())  # same as ' '

sentence = "Hello*python*class*vip"
print(f"'{sentence}'", sentence.split('*'))

################# remove spaces from start + end
sentence = "   Hello, World!!   "
print(f"'{sentence}'", 'strip=', sentence.strip())
print(f"'{sentence}'",sentence.split())

################# upper -> lower, lower -> upper
print(f'{"AasdasBcccC".swapcase()}', "AasdasBcccC".swapcase().swapcase())
#         aASDASbCCCc
print()

sentence = "Hello, World!! good morning"
print(sentence)
print('sentence.startswith("Hello") ?', sentence.startswith("Hello"))

print('sentence.endswith("morning") ?', sentence.endswith("morning"))

############ make the first letter upper case, all other lower case
text8 = "hello, world!! Good morning"
#        Hello, world!! good morning
print('text8.capitalize() ', text8.capitalize())

############ each new word starts with upper case, all other lower case
text9  = "hello, world!! good morNing"
#         Hello, World!! Good Morning
print('text9.title() ', text9.title())

############ is alpha checks if the expression is only letters
print("1234.isalpha()" , "1234".isalpha())
print('"abcd".isalpha()', "abcd".isalpha())
print('"abcd_".isalpha()', "abcd_".isalpha())
print('"abcd*".isalpha()', "abcd1*".isalpha())

print('"1234.isdigit()', "1234".isdigit())
print('"abcd".isdigit()" ', "abcd".isdigit())
print('"abcd1".isdigit()" ', "abcd1".isdigit())

print('"Aab".islower()', "Aab".islower())
print('"aab".islower()', "aab".islower())
print('"Aab".isupper()', "Aab".isupper())
print('"ABC".isupper()', "ABC".isupper())

print('"42".zfill(5)', "42".zfill(5))

print('123456789ABC')
print(f"{'Hello!'.center(11, '-')}hi")
print('Hello!'.center(11, ' '))

print('"     ".isspace()', "    ".isspace())

print("Hello python course")
#                 0123456789012345678
print('    [0]', "Hello python course"[0])
print('   [-1]', "Hello python course"[-1])
#                 0123
print("  [0:3]", "Hello python course"[0:3])  # 0-3 not include 3
print("  [1:4]", "Hello python course"[1:4])  # 1-4 not include 4
#                 0123456789012345678
print("[1:8:2]", "Hello python course"[1:8:2])  # 1-8 not include 8
print("  [0:4]", "Hello python course"[0:4])  # 0-4 not include 4
print("   [:4]", "Hello python course"[:4])  # 0-4 not include 4
print(len("Hello python course"))  # 19
print(" [0:19]", "Hello python course"[0:19])  # 0-end
print("   [0:]", "Hello python course"[0:])  # 0-end
print("    [:]", "Hello python course"[:])  # 0-end
print("  [::2]", "Hello python course"[::2])  # 0-end jump 2
print(" [::-1]", "Hello python course"[::-1])  # 0-end jump 2

'''
1
name = "Danny"
# Fix this line:
print(f"{name} your name is in length len(name)")

2
first_name = "Petros"
last_name = "Borchardt"
id_num = "63 251283 B 185"
phone = "0419-0288803"

# Expected Output Layout: (use center)
# |   Borchardt, Petros   | 
# | ID: [63 251283 B 185] | 
# | Phone: 0419-0288803   |

full_name = f"{last name}, {first_name}"
print(f"| {full_name.center(22)} |")

3
Given the dirty input string user_input = "   jOhN_dOe_2026   ", 
write python expressions to:Remove the leading and trailing whitespaces
Convert the entire string to lowercase
Replace all underscores (_) with hyphens (-)

4
answer True/False
print("python3".isalpha())
print("12 34".isdigit())
print("   ".isspace())
print("HELLO".isupper())
print("hi".islower())

5
msg = "step on no pets"
check if we reverse this str we get the same string 

6
Given the string course = "Python Core Study Mechanics"
check if the first word "Python"
check if the last word "Mechanics"
split this sentence into a string of words and print it 

7
"Python Core Study Mechanics"
run on this string , print each character in a new line using a for loop
don't print space
'''
