import sys

# Initial conditions
init_vel = 20  # Initial velocity in m/s (change this to simulate different speeds)
init_height = 0  # Initial height in meters (change this to simulate different heights)
g = 9.81  # Acceleration due to gravity in m/s^2
time = 0  # Start time
dt = 0.01  # Time step
vel = init_vel  # Set initial velocity
pos = init_height  # Set initial position
tempPos = pos  # To track the maximum height

run = True
while run:
    # Store previous position
    tempPos = pos
    
    # Update velocity (velocity decreases because of gravity)
    vel -= g * dt
    
    # Update position
    pos += vel * dt
    
    # Update time
    time += dt
    
    # Check if the ball is falling down (position starts to decrease)
    if pos < tempPos:
        print(f"Maximum height reached: {tempPos:.2f} meters, Time: {time:.2f} seconds")
        run = False
    
    # Stop the simulation if the ball hits the ground
    if pos <= 0:
        print(f"Ball has hit the ground at time: {time:.2f} seconds")
        run = False

sys.exit()
