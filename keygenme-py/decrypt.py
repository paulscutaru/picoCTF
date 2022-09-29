import hashlib
username_trial = 'PRITCHARD'
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
dec =''.join([hashlib.sha256(username_trial.encode()).hexdigest()[i] for i in [4,5,3,6,2,7,1,8]])
key_full_template_trial = key_part_static1_trial + dec + key_part_static2_trial
print(key_full_template_trial)