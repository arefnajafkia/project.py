# Fibonachi

def  fib (N):
        #'Calculate Fibonachi Series'
       fib = [ 0, 1]
       for i in range(N):
            fib.append(fib[-2]+fib[-1])
       return  fib
        
N = int (input("N = "))
print(fib(N))
