from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'calculate.html', locals())
    
def calculate_n(request):

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1) 
             
    if request.method == "POST":
        if 'calculated_n_input' in request.POST:
            smth = int(request.POST['calculated_n_input'])
            calculated_n_result = factorial(smth)
            
        return render(request, 'calculate.html', {'result': calculated_n_result})      
        
def calculate_fib(request):

    def fib(n):
        if n == 0: return 0
        elif n == 1: return 1
        else: return fib(n-1)+fib(n-2)

    if request.method == "POST":
        if 'calcfib_input' in request.POST:
            smth = int(request.POST['calcfib_input'])
            calculated_fib = fib(smth)    
        return render(request, 'calculate.html', {'calculated_fib': calculated_fib})      
        
       
def calculate_primes(request):
    
    def primez(n):   
        import math
        result = []
        for num in range(1, n):
            if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
               result.append(num)
        return result
    
    if request.method == "POST":
        if 'calcprimes_input' in request.POST:
            smth = int(request.POST['calcprimes_input'])
            calculated_primes = primez(smth)    
        return render(request, 'calculate.html', {'calculated_primes': calculated_primes})                
 
 
      
def encode(text):
	if not text:
		return ""
	else:
		last_char = text[0]
		max_index = len(text)
		i = 1
		while i < max_index and last_char == text[i]:
			i += 1
		return last_char + str(i) + encode(text[i:])

def decode(text):
	if not text:
		return ""
	else:
		char = text[0]
		quantity = text[1]
		return char * int(quantity) + decode(text[2:])
 
       
       
       
       
       
       
       
       
        
        
        
        
        
        
        
        
        
