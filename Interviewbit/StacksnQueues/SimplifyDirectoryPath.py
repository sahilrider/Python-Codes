'''https://www.interviewbit.com/problems/simplify-directory-path/'''
class Solution:
    def simplifyPath(self, A):
        A = A + '/'
        l = A.split('/');
        m = []
        m.append('/')
        for i in range(1,len(l)-1):
            if l[i] == ".." and len(m)>1:
                m.pop()
            elif l[i] == ".." and len(m)==1:
                continue
            elif l[i] == ".":
                continue
            elif l[i] != '':
                m.append('/'+str(l[i]))
        if len(m) == 1:
            return '/'
        return (''.join(m))[1:]