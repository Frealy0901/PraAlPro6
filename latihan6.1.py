# Mendefinisikan 
def prima(bil):
    kelipatan = 2
    for i in range(bil-1,2,-1):
        while i >= kelipatan:                      # Mengulang terus sampai i >= dengan kelipatan atau 2
            if i == kelipatan:                     # Jika i sudah sama dengan Kelipatan atau 2                  
                return i                           # maka di return atau dikembalikan ke i
            else:                                  # Jika tidak sama dengan kelipatan atau 2
                if i % kelipatan == 0:             # Jika i dimod kelipatan == 0 maka akan di stop atau break
                    break
                else:                              # Jika i mod kelipatan tidak sama dengan 0 
                    kelipatan += 1                 # Kelipatan ditambah sama dengan i
                    continue                       # Skip atau melanjutkan 
                   
print(prima(12))