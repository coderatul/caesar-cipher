![Bold Red LinkedIn Post Header](https://user-images.githubusercontent.com/72141859/151677664-7e46fc4b-fa83-4f21-bd08-750bf439e504.png)

# Caesar Cipher
- In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
- example 
```
plain text : atul is coder
cipher txt : dwxo lv frghu
if shifted 3 characters to right 
```
- The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A → 0, B → 1, ..., Z → 25. Encryption of a letter x by a shift n can be described mathematically as
```
encryption(x) = (x + n) % 26
```
- Decryption is performed similarly,
```
decyption(x) = (x - n) % 26
