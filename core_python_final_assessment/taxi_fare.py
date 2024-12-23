def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare
def calculate_total_fares(trips):
    fares = [calculate_fare(distance) for distance in trips]
    total_fare = sum(fares)
    return fares, total_fare

trips = [5, 10, 3]  
fares, total_fare = calculate_total_fares(trips)
for i, fare in enumerate(fares, start=1):
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total_fare}")
