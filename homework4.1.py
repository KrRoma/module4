def palindrom(s):
    k=0
    for i in range(len(s)//2):
        if s[i]==s[-1]:
            s=s[:-1]
        else:
            k=1
            break
    if k==1:
        print('False')
    else:
        print('True')
palindrom('лепсспел')
