import time

def merge_sort(flights):
  if len(flights) > 1:
    mid = len(flights) // 2  # Find middle index
    left_half = flights[:mid] # Divide list into halves
    right_half = flights[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i][1] < right_half[j][1]:
        flights[k] = left_half[i]
        i += 1
      else:
        flights[k] = right_half[j]
        j += 1
      k += 1
    while i < len(left_half):
      flights[k] = left_half[i]
      i += 1
      k += 1

      while j < len(right_half):
        flights[k] = right_half[j]
        j += 1
        k += 1
      

# Take user input
num_flights = int(input("Enter number of flights: "))
flights = []
for _ in range(num_flights):
  flight_no = input("Enter the flight number: ")
  dept_time = int(input(f"Enter departure time for {flight_no}: "))
  flights.append((flight_no, dept_time))


# Measure the execution time
start_time = time.time()
merge_sort(flights)
end_time = time.time()

print("Flights sorted by departure time: ", flights)
print(f"Execution time: {end_time - start_time:.6f} seconds")
