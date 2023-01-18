#6.5 Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0')
#print(x) remember''
y = text[x:]
#print(y)
z = float(y)
print(z)
