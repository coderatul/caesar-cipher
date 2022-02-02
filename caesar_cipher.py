print(r"""
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                               
""")
#caesar cipher encryption
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("enter alphabets only !")
encode = input("enter txt to be encrypted: ").replace(" ","").casefold()
assert encode.isalpha(),"/* only alphabets allowed */"
shift = int(input("how many character would you like to shift: "))
encrypted_r =""
encrypted_l =""
for i in encode:
    index_r = (alphabets.index(i)+shift)%26
    encrypted_r += alphabets[index_r]
    index_l = (alphabets.index(i)-shift)%26
    encrypted_l += alphabets[index_l]
print("{} when shifted {} character form right: {}".format(encode,shift,encrypted_r))
print("{} when shifted {} character form left: {}".format(encode,shift,encrypted_l))

#caesar cipher decryption
decode = input("enter caesar cipher encoded text: ").replace(" ","").casefold()
assert decode.isalpha(),"/* only alphabets allowed */"
Shift = int(input("how may characters where shifted: "))
print("if shift was from left enter : l")
print("if shift was from right enter : r")
left_or_right = input("wether shift was from left or right: ").replace(" ","").casefold()
decrypted_r =" "
decrypted_l=" "
for k in decode:
    Index_r = (alphabets.index(k) - Shift) % 26
    decrypted_r += alphabets[Index_r]
    Index_l= (alphabets.index(k) + Shift) % 26
    decrypted_l += alphabets[Index_l]
if left_or_right == "l":
  print("{} when shifted {} character form left: {}".format(decode,shift,decrypted_l))
elif left_or_right== "r":
  print("{} when shifted {} character form right: {}".format(decode,shift,decrypted_r))
