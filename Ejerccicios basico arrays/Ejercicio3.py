favorite_foods = ["pizza", "ice cream", "cheeseburgers"];
favorite_foods.insert(0, "pasta");
favorite_foods.append("sushi");
print ("Ejercicio 3: " + str(favorite_foods));
print ("Ejercicio 4: " + str(favorite_foods[1]));
print ("Ejercicio 5: " + str(favorite_foods[-1]));
favorite_foods.insert(1, "pepperoni");
print ("Ejercicio 6: " + str(favorite_foods[1]));
favorite_foods.__delitem__(-1);
print ("Ejercicio 7: " + str(favorite_foods));
# Ejercicio 8
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print ("Ejercicio 9: " + str(numbers[:5]));
print("Ejercicio 10: ")
for i in numbers:
    if i % 2 == 0 :
        print(str(numbers[i - 1]));
print("Ejercicio 11: ");
for i in numbers:
    if i % 2 != 0 :
        print(str(numbers[i - 1]));
print("Ejercicio 12: " + str(numbers[4::5]));

