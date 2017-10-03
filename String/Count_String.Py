import re  #Regular Expressions Module
def count_substring1(string, sub_string):
    p=re.compile(sub_string)
    a=p.findall(string)
    return len(a)

def count_substring2(string, sub_string):
    c=0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            c+=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring1(string, sub_string)
#   count=count_substring2(string,sub_string)
    print(count)
