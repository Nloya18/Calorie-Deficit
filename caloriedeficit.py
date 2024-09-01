age = int(input("age: "))
height = input("height(5' 8\"): ")
weight = int(input("weight: "))
sex = input("M or F: ").upper()
print("\n Select Your Current Activity:")
print("1.) Sedetary::Little or no exercise")
print("2.) Light: Exercise 1-3 times")
print("3.) Moderate: Moderate exercise 4-5 times")
print("4.) Active: daily exercise or intese exercise 3-5 times")
print("5.) Very Active: intense exercise 6-7 times")
num = int(input("1, 2, 3, 4, or 5: "))

def activity(num, bmr):
    if num == 1:
        return bmr * 1.2
    elif num == 2:
        return bmr * 1.375
    elif num == 3:
        return bmr * 1.55
    elif num == 4:
        return bmr * 1.725
    elif num == 5:
        return bmr * 1.9
    else:
        raise ValueError("Incorrect number inputted for activity")

        
def toKilos(weight):
    kilograms = weight * 0.45359237
    return kilograms

def toInches(w):
    if len(w) == 1:
        inches = int(w) * 12
        return inches
    elif len(w) > 1 and len(w) <= 4:
        if ' ' in w:
            feet = int(w.partition(' ')[0])
            inch = int(w.partition(' ')[2])
            inches = (feet * 12) + inch
            return inches
        else:
            raise ValueError("Incorrect Height Format")
            
    else:
        raise ValueError("Incorrect Height Format")
        
def toCentimeters(inches):
    centimeters = inches * 2.54
    return centimeters

def bmr(age, height, weight, sex):
    if 'M' in sex:
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
        return bmr
    if "F" in sex:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
        return bmr
    else:
        raise ValueError("Incorrect sex choose M or F")
    
def macros(tdee, plan, mild, regular, extreme):
    if plan == 1:
        tdee = tdee - 0
    if plan == 2:
        tdee = tdee - mild
    elif plan == 3:
        tdee = tdee - regular
    elif plan == 4:
        tdee = tdee - extreme
    else:
        raise ValueError("Incorrect number inputted for plan")

    protein_percentage = 0.30
    fat_percentage = 0.25
    carbs_percentage = 0.45
    
    protein_calories = tdee * protein_percentage
    fat_calories = tdee * fat_percentage
    carbs_calories = tdee * carbs_percentage

    protein_grams = protein_calories / 4
    fat_grams = fat_calories / 9
    carbs_grams = carbs_calories / 4

    return protein_grams, fat_grams, carbs_grams

def calculate_weight_loss():
    mild = 0.5
    regular = 1
    extreme = 2
    mild_deficit = (mild * 3500) / 7
    regular_deficit = (regular * 3500) / 7
    extreme_deficit = (extreme * 3500) / 7

    return mild_deficit, regular_deficit, extreme_deficit
kg = toKilos(weight)
inches = toInches(height)
cm = toCentimeters(inches)

BMR = int(bmr(age, cm, kg, sex) + 0.5)
TDEE = int(activity(num, BMR) + 0.5)
mild, regular, extreme = calculate_weight_loss()

print("\nSelect wieght loss plan:")
print("1.) Calories to maintain weight:", TDEE)
print("2.) Calories for 0.5lb weight loss per week:", TDEE - mild)
print("3.) Calories for 1lb weight loss per week:", TDEE - regular)
print("4.) Calories for 2lb weight loss per week:", TDEE - extreme)
plan = int(input("Pick a desired plan: "))
protein, fat, carbs = macros(TDEE, plan, mild, regular, extreme)

print(f"\nRecommended Macros:")
print(f"Protein: {protein:.0f} grams/day")
print(f"Fat: {fat:.0f} grams/day")
print(f"Carbohydrates: {carbs:.0f} grams/day")