def triangle_type(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return "Pas un triangle"
    elif a == b == c:
        return "triangle équilatéral"
    elif a == b or b == c or c == a:
        if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
            return "triangle isocèle et triangle rectangle"
        else:
            return "triangle isocèle"
    elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
        return "triangle rectangle"
    else:
        return "triangle scalène"

a, b, c = 4, 4, 4
print(triangle_type(a, b, c))
 
a, b, c = 3, 3, 4.24
print(triangle_type(a, b, c))
 
a, b, c = 5, 5, 7
print(triangle_type(a, b, c))
 
a, b, c = 3, 4, 5
print(triangle_type(a, b, c))
 
print(triangle_type(a, b, c))
 
a, b, c = 1, 2, 4
print(triangle_type(a, b, c))
