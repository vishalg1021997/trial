user = {'vishal':[1000,9819287727,['abc','deff','ghi']],
        'nilesh':[1000,8169115870,['qwe','wer','erty']],
        'kanishka':[1000,123456789,['rty','tyu','rtt']],
        'ananya':[1000,987654321,['rtyy','tyyu','rytt']]}

a= input()
user['vishal'][0] = + 1000
print(user)
if a in user:
    print(True)

    print(user.get(a))
else:
    print(False)