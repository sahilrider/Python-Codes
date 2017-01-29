def is_anagram(s1,s2):
    t1=list(s1)
    t2=list(s2)
    if len(s1)!=len(s2):
        return False
    for i in range(len(t1)):
        if t1[i] not in t2:
            return False
        else:
            t2.remove(t1[i])
    return True

print(is_anagram('sahil','slaih'))
