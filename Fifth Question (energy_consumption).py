def energy(readings):
    for r in readings:
        if r < 10 or r > 200:
            print("INVALID INPUT")
            return
    
    sensor_totals = [0] * 5
    
    for i in range(20):
        sensor_totals[i % 5] += readings[i]
    
    sensor_averages = [round(total / 4) for total in sensor_totals]
    max_avg = max(sensor_averages)
    
    if max_avg < 50:
        print("Energy consumption is optimal.")
    else:
        print("Sensor Number :", sensor_averages.index(max_avg) + 1)

readings = []
for i in range(5):
    for j in range(4):
        readings.append(int(input(f"Enter power reading for Sensor {i+1}, Time {j+1}: ")))
    
if len(readings) != 20:
    print("INVALID INPUT")

energy(readings)



