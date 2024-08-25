# Encoder and Decoder-Project 

# Overview
This Python program provides a simple text encoding and decoding functionality. It takes user input and applies a custom encoding scheme to scramble the text, and also provides a decoding function to reverse the process.

# How to Use
1. Run the program and choose whether you want to encode (E) or decode (D) text. <br>
2. Enter the text you want to encode or decode. <br>
3. The program will output the encoded or decoded text. <br>

# Encoding Scheme. <br>
- The encoding scheme works by taking each word in the input text and applying the following rules: <br>

If the word has 3 or more characters, it generates a random string of 26 characters, takes the first 3 characters of the random string, appends the word (excluding the first character), appends the first character of the word, and finally appends the next 3 characters of the random string.
If the word has less than 3 characters, it simply reverses the word. <br>

# Decoding Scheme
- The decoding scheme works by reversing the encoding process:

If the word has 3 or more characters, it extracts the original word by taking the substring from index 3 to -3, and then moves the last character to the front.
If the word has less than 3 characters, it simply reverses the word. <br>

# Example
Encoding: Input "Hello World" and the program will output a scrambled version of the text, such as "kJdHllo Wdlro".
Decoding: Input the encoded text "kJdHllo Wdlro" and the program will output the original text "Hello World".
