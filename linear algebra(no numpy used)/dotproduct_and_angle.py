import math

def dotproduct(m,n):
    if len(m) != len(n):
        raise ValueError("Different dimensions")
    result = 0
    for i in range(len(m)):
        result += m[i] * n[i]
    return result

def norm(v):
    return math.sqrt(sum(x*x for x in v))

def angle(v,x):
    cos_theta = dotproduct(v,x)/ (norm(v) * norm(x))
    cos_theta = max(-1.0,min(1.0,cos_theta))
    theta = math.acos(cos_theta)
    angle = theta * 180/math.pi
    return angle

#test
a = [1,-5,0]
b = [2,-10,0]

print(f"Dot produnct: {dotproduct(a,b)}")
print(f"Angle between them: {angle(a,b):.2f} degrees")

