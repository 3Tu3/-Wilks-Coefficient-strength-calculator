def calculate_wilks_coefficient(weight_lifted, body_weight, is_male):
    if is_male:
        a = -216.0475144
        b = 16.2606339
        c = -0.002388645
        d = -0.00113732
        e = 0.00000701863
        f = -0.00000001291
    else:
        a = 594.31747775582
        b = -27.23842536447
        c = 0.82112226871
        d = -0.00930733913
        e = 0.00004731582
        f = -0.00000009054

    coefficient = weight_lifted * (500 / (a + b * body_weight + c * body_weight**2 + d * body_weight**3 + e * body_weight**4 + f * body_weight**5))
    return coefficient
    
def calculate_level(wilks_coefficient):
    if wilks_coefficient < 25.6:
        return "Beginner (1)"
    elif wilks_coefficient < 31.9:
        return "Novice (2)"
    elif wilks_coefficient < 38.8:
        return "Intermediate (3)"
    elif wilks_coefficient < 48.55:
        return "Advanced (4)"
    elif wilks_coefficient < 58.3:
        return "Expert (5)"
    elif wilks_coefficient < 69.55:
        return "Master (6)"
    elif wilks_coefficient < 80.8:
        return "Grand Master (7)"
    elif wilks_coefficient < 92.05:
        return "Legend (8)"
    elif wilks_coefficient < 102:
        return "Titan (9)"
    else:
        return "Elite (10)"

weight_lifted = 50
body_weight = 25
is_male = True

w = weight_lifted
bw = body_weight
x = 0
while bw * x < w:
    x = x + 0.00001
    
wilks_coefficient = calculate_wilks_coefficient(weight_lifted, body_weight, is_male)
level = calculate_level(wilks_coefficient)

print("Weight lifted:", weight_lifted, "kg")
print("Body weight:", body_weight, "kg")
print("lift to body weight percentage",  x * 100, '%')        
print("Lift x Body Weight", x)
print("Wilks Coefficient:", wilks_coefficient)
print("Level:", level)
