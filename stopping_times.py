'''
This file was used to generate the graph of stopping times as shown in the Streamlit

Maverick Reynolds
'''

import matplotlib.pyplot as plt
from Collatz import collatz

def collatz_stops(n):
    return [len(collatz(i)) - 1 for i in range(1, n + 1)]

def graph_stops():
    # Generate the graph
    plt.plot(collatz_stops(100_000), ls='none', marker='.', markersize=1, color='red')
    plt.xlabel('Input')
    plt.ylabel('Stopping Time')
    plt.title('Stopping Times for the First 100,000 Positive Integers')
    plt.savefig('stopping_times_100K.png')
    plt.show()

