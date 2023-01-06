import string

sentence = 'Notice!! He was the one who said" wow!! this is great!!"'
list = [c for c in sentence if c not in string.punctuation]
with_out_punc = ''.join(list)
with_out_punc_list = ''.join(list).split()
print(with_out_punc)
print(with_out_punc_list)
