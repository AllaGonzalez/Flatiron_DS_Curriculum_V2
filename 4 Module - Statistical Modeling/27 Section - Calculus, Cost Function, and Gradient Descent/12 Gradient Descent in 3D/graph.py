import matplotlib.pyplot as plt
import numpy as np

def func_1(x,coef):
    return coef * x**2
def func_2(y,coef):
    return y * coef **2

def deriv(f,x,co):

    h = 0.000000001
    return np.round((f(x+h,co) - f(x,co))/h,1)

def tan_plot(f,x,co):
    x_vals = np.linspace(x - 0.9,x+0.9,100)
    slope = deriv(f,x,co)
    tan = f(x,co)+slope*(x_vals-x)
    y = f(x,co)
    return (slope,x_vals, tan,y)

def make_plots(func):
    coefs = [-1,1,2,3]
    colors = ['g','r','c','m']
    plt.figure(figsize=(14,14))
    for coef_idx, coef in enumerate(coefs):
        x_list = [0,1,3,5]
        ax = plt.subplot(2,2,coef_idx+1)
        ax.plot(np.linspace(-7,7,100), func(np.linspace(-7,7,100),coef),alpha=0.25)
        sub_label = 'f(x,{c}) = {c} * x^2'.format(c=coef)
        ax.set_title(sub_label)
        if np.sign(coef) > 0:
            ax.set_ylim(-4,100)
        else:
            ax.set_ylim(-100,4)
        for color_idx,x_val in enumerate(x_list):
            m,x,tan,y = tan_plot(func,x_val,coef)
            ax.plot(x_val,y,marker='o',color=colors[color_idx])
            ax.plot(x,tan,label='slope ={}'.format(m),color=colors[color_idx])
        ax.legend()
    plt.show()


def make_plots_2(func):
    coefs = [-1,1,2,3]
    colors = ['g','r','c','m']
    plt.figure(figsize=(14,14))
    for coef_idx, coef in enumerate(coefs):
        x_list = [0,1,3,5]
        ax = plt.subplot(2,2,coef_idx+1)
        ax.plot(np.linspace(-7,7,100), func(np.linspace(-7,7,100),coef),alpha=0.25)
        sub_label = 'f(y,{c}) = y * {c}^2'.format(c=coef)
        ax.set_title(sub_label)
        for color_idx,x_val in enumerate(x_list):
            m,x,tan,y = tan_plot(func,x_val,coef)
            ax.plot(x_val,y,marker='o',color=colors[color_idx])
            ax.plot(x,tan,label='slope ={}'.format(m),color=colors[color_idx])
        ax.legend()
    plt.show()
make_plots_2(func_2)
