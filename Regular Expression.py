
import re # res stands for regualar expression

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map
+917410760563
Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''




'''function in regular expression are as follow 
findall, search, split, sub, finditer
'''





########################META CHARACTER##################################################################################




'''THIS IS THE SIMPLE WAY TO USE METHOD'''
# print(re.findall("Fax",mystr)) #it return the list of found elements
# print(re.search("Fax",mystr))  #it returns the map object if the object is found
# print(re.split("Fax",mystr)[0]) # split the string

'''THIS IS A EASY WAY '''

ok=re.compile(".rect")  # compile the object of regular expression with some words

# print(ok.search(mystr))  #it return map object
# print(ok.findall(mystr)) #it return string

# patt=re.compile("^Tata")  #    ^  return match object if the string start  with the given string
# patt=re.compile("ii$")    #    $  return match objcet if the string ends with the given string
# patt=re.compile("ai*")    #    *  return match objcet if zero or more occurance are found
# patt=re.compile("ai+")    #    +  return match objcet if one or more occurance are found
# patt=re.compile("ai{2}")  #   {}  return match objcet for exactly number of occurance
# patt=re.compile("(ai){2}")#   ()  return match objcet for exactly number of occurance for a group which lies with parenthesis
# patt=re.compile("(ai){1}|t")#    |  or of the string provided



##################################################SPECIAL SEQUENCE#####################################################


patt=re.compile(r'\ATata')        # \A starts with the given string
patt=re.compile(r'\bFax')         # \b words starts with the given string
patt=re.compile(r'Fax\b')         # \b words ends with the given string
patt=re.compile(r'\d{5}-\d{4}')   # \d return the string by taking number of digit
patt=re.compile(r"91\d{10}")      # \d return the string by taking number of digit
patt=re.compile(r"\Bax")          #  \B word
patt=re.compile(r"\D")

matches=patt.finditer(mystr)

for match in matches:
    print(match)