import math

def banana_camel_problem(start_bananas, capacity, distance):
    current_bananas = start_bananas
    current_distance = 0
    total_distance_traveled = 0  
    total_bananas_consumed = 0   
    while current_distance < distance:
        trips = 2 * math.ceil(current_bananas / capacity) - 1
        trip_distance = min(distance - current_distance, capacity / trips)
        bananas_consumed = trips * trip_distance
        current_bananas -= bananas_consumed
        current_distance += trip_distance
        total_distance_traveled += trips * trip_distance
        total_bananas_consumed += bananas_consumed
        print(f"Distance to destination: {distance - current_distance}, Bananas remaining: {current_bananas}")
    path_cost = total_bananas_consumed
    total_time_taken = total_distance_traveled
    return current_bananas, path_cost, total_time_taken
if __name__ == "__main__":
    start_bananas = int(input("Enter the initial number of bananas: "))
    capacity = int(input("Enter the camel's carrying capacity: "))
    distance = int(input("Enter the distance to the destination: "))
    max_bananas, path_cost, total_time_taken = banana_camel_problem(start_bananas, capacity, distance)
    print(f"Maximum bananas at the destination: {max_bananas}")
    print(f"Total bananas consumed (Path Cost): {path_cost}")
    print(f"Total distance traveled (Total Time Taken): {total_time_taken}")