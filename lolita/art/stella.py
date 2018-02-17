from stellar_base.address import Address as STELLAR








publickey = 'GDVDKQFP665JAO7A2LSHNLQIUdsNYNAAIGJ6FYJVMG4DT3YJQQJSRBLQDG'
address = STELLAR(address=publickey) # address = Address(address=publickey,network='public') for livenet
print(address[0])
