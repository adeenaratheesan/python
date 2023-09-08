# ************************ programe to generate a sine wave pattern using asterisks******************
import math

# Set the parameters for the sine wave
amplitude = 10
frequency = 10

# Define the size of the grid
width =180
height =120

# Create a blank grid
grid = [[' ' for _ in range(width)] for _ in range(height)]

# Calculate the sine wave and fill in the grid
for x in range(width):
    # Calculate the corresponding y-coordinate in the sine wave
    y_wave = int(amplitude * math.sin(frequency * (2 * math.pi * x / width)) + height // 2)
    
    # Place '*' characters at points on the sine wave curve
    grid[y_wave][x] = '*'

# Print the grid
for row in grid:
    print(''.join(row))
