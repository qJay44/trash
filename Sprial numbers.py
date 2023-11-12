import matplotlib.pyplot as plt
import numpy as np


def main(amount, showIntergers=True, showPrimary=True):
    integers = np.arange(0, amount, 1)
    primary = np.array([n for n in integers if isPrime(n) and n not in (0, 1)])
    theta_i = 1 * integers
    theta_p = 1 * primary
    
    showPlot(integers, primary, theta_i, theta_p, showInt=showIntergers, showPrim=showPrimary)


# Checking if number is prime
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(np.sqrt(n)) + 1, 2))


def showPlot(integers, primary, *angles, **plots):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(9, 9), dpi=110, facecolor='#161616')
    ax.set_facecolor('black')
    ax.tick_params(axis='both', colors='white', labelsize=9)
    ax.set_aspect(1)
    
    # Hiding plots if necessary 
    if plots['showInt']: 
        ax.scatter(angles[0], integers, s=2, c='#03071e', label='Integer numbers')
    if plots['showPrim']:
        ax.scatter(angles[1], primary, s=2, c='#590d22', label='Primary numbers')

    ax.set_yticklabels([])
    ax.legend(loc='center right', bbox_to_anchor=(1.1, 1), fontsize='x-large', labelcolor='white',
              markerscale=6.0,  handletextpad=0.6, handlelength=0.9, handleheight=1.2, facecolor='#343a40')
    ax.grid(False)
    ax.set_title("Numbers on the polar coordinates\nWhere (x, \u03B8) = (n, n)", va='bottom', 
                color='white',
                fontsize=20, 
                fontname='Cambria',
                fontstyle='italic'
    )
    plt.show()

if __name__ == '__main__':
    """Program start
    
    1. Number of dots
    2. Show integer numbers (default is True)
    3. Show primary numbers (default is True)
    
    """
    main(10000)
    