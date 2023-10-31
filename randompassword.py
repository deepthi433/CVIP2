import random
Lower="abcdefghijklmnopqrstuvwxyz"
Upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Special_char="!@#$%^&*()"
Numbers="1234567890"
string = Lower+Upper+Special_char+Numbers
length = 10
password="". join(random.sample(string,length))
print("The random password generated:",password)