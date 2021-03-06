"""You throw a ball vertically upwards with an initial speed v (in km per hour). The height h of the ball at each time t is given by h = v*t - 0.5*g*t*t where g is Earth's gravity (g ~ 9.81 m/s**2). A device is recording at every tenth of second the height of the ball. For example with v = 15 km/h the device gets something of the following form: (0, 0.0), (1, 0.367...), (2, 0.637...), (3, 0.808...), (4, 0.881..) ... where the first number is the time in tenth of second and the second number the height in meter.

Task
Write a function max_ball with parameter v (in km per hour) that returns the time in tenth of second of the maximum height recorded by the device.

Examples:
max_ball(15) should return 4

max_ball(25) should return 7

Notes
Remember to convert the velocity from km/h to m/s or from m/s in km/h when necessary.
The maximum height recorded by the device is not necessarily the maximum height reached by the ball.
"""


## My solution: I'm getting most of the test cases right, I must have a rounding error somewhere as a couple are off by 1.

def max_ball(v0):
  results  = []
  for t in range(0, 10):
    
    t = t/10
    v = v0 * 0.278  #multiply by 0.278 to convert to meters/s
    g = 9.81
    h = (v * t) - (.5 * g * t ** 2)
    results = results + [[h , t]]
  
  big = max(results)
  big = (big[1]) * 10
  return int(big)
  
  ##Best solution:
  
  def max_ball(v0):
    return round(10*v0/9.81/3.6)
