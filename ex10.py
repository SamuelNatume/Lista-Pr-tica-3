lista=[2,3,2,5,4,3,7,2,9,4,1,4]

num_rep = 0
num_freq = 0

for num in lista:
   if lista.count(num) > num_freq:
      num_freq += 1
      num_rep = num
print(f"O Número mais repetido é o {num_rep}, pois apareceu {num_freq} vezes")    
