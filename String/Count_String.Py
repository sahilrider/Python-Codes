import re  #Regular Expressions Module
'''
..Function compile()

It compiles regular expression pattern into a regular expression object, which can be used for matching using its match() and search() methods.

..Function findall()
It return all non-overlapping matches of pattern in string, as a list of strings.

For much detailed explanation -->
https://docs.python.org/2/library/re.html
'''
def count_substring(string, sub_string):
    c=0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            c+=1
    return c

def count_substring1(string, sub_string):
    p=re.compile(sub_string)
    a=p.findall(string)
    return len(a)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring1(string, sub_string)
#  
    print(count)


