s = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
s2 = ''
for c in s:
	index = alphabet.find(c)
	if index == -1:
		s2 += c
	else:
		s2 += alphabet[index+13]
print(s2)