import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
    return x*y**2

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 500, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
fig = plt.figure()
plt.show()




import plotly
from plotly.graph_objs import Scatter, Layout
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML

init_notebook_mode(connected=True)
x_values = list(range(0, 6))

def linear_function(x, constant):
    return x*constant
one_x = list(map(lambda x_value: linear_function(constant=3, x=x_value), x_values))
trace_1 = Scatter(x=x_values, y=one_x, name="function_1 = x")

layout = Layout(title="Direction of gradient ascent", autosize=False, xaxis=dict(
        range=[0, 6]
    ),
    yaxis=dict(
        range=[0, 6]
    )
)

plotly.offline.iplot({
    "data": [trace_1],
    "layout": layout
})
