import numpy as np
import control as ctrl

# Define the plant transfer function (a second-order system with uncertain parameters)
num = [1]
den = [1, 1, 1]  # A third-order denominator for illustration purposes
plant = ctrl.TransferFunction(num, den)

# Define the reference model (desired system dynamics)
ref_model = ctrl.TransferFunction([1], [1, 2, 1])

# Initialize the adaptive control algorithm
adapt_ctrl = ctrl.adaptive.AdaptiveControl(plant, ref_model)

# Define the time vector for simulation
t = np.linspace(0, 10, 100)

# Run the adaptive control algorithm
y, t, x = ctrl.forced_response(adapt_ctrl, T=t)

# Plot the response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Adaptive Control System Response')
plt.grid(True)
plt.show()
