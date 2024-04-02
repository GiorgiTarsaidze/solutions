def tribonacci(signature, n):
    if not n:
        return []
    
    if n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    
    for i in range(n-3):
        signature.append(signature[i] + signature[i+1] + signature[i+2])
    
    return signature