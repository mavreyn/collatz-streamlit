'''
So This is the perfect hello world program for data visualization / computer science
Taking this old thing and making it new again

Maverick Reynolds
06.10.2023
'''

import streamlit as st
from PIL import Image

@st.cache_data
def collatz(z):
    steps = [z]

    while z != 1:
        if z % 2 == 0:
            z //= 2
        else:
            z = 3*z + 1

        steps.append(z)
        
    return steps

def main():
    # Information about the app
    st.title('Interactive Collatz')
    st.write('Made by Maverick Reynolds')

    st.subheader('About')
    st.write('This interactive allows a user to input a number and see the Collatz sequence for that number. The sequence is defind by a simple relation as shown below:')

    st.write('''
    $$
    f(n) =
    \\begin{cases}
    n/2, & \\text{if } n \\text{ is even} \\\\
    3n + 1, & \\text{if } n \\text{ is odd}
    \\end{cases}
    $$
    ''')
    
    st.write('The Collatz conjecture states that for any positive integer, the sequence will always reach *1*. Use the sidebar to enter a number and see the sequence displayed.')

    # Make a sidebar for input
    st.sidebar.title('Enter an Integer:')
    z = st.sidebar.number_input('', 1, step=1)

    # Display the sequence
    st.subheader('The Collatz Sequence for *' + str(z) + '*:')

    coll_output = collatz(z)

    # Display the graph
    st.line_chart(coll_output)

    # Raw List
    if st.checkbox('Show raw list'):
        st.write(coll_output)

    st.header('Importance of Iterations')
    st.write('The number of iterations it takes to reach *1* is called the stopping time. The stopping time for *' + str(z) + '* is *' + str(len(coll_output) - 1) + '*. As the value of the input increases, the stopping time generally tends to increase. The stopping time for the first 1000 positive integers is shown below:')

    # Display the graph using matplotlib (use image)
    stops_img = Image.open('stopping_times_100K.png')
    st.image(stops_img, use_column_width=True)

    st.subheader('Interesting Observations')
    st.write('As the numbers increase, the trivial lower bound follows the curve $y=log_2(x)$ because the quickest reduction would occur if the number passed through is a power of *2* so that at every iteration we are dividing by *2* to get to *1*. The upper bound is much harder to predict. and is still an open problem.')
    st.write('In addition, the graph shows some very peculiar curves which are quite satisfying to look at.')

    st.header('Other Resources')
    st.write('For more information on the Collatz conjecture, check out the following links:')
    st.write('**Wikipedia** https://en.wikipedia.org/wiki/Collatz_conjecture')
    st.write('**Numberphile** https://www.youtube.com/watch?v=5mFpVDpKX70')
    st.write('**Quanta Magazine** https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922')

    



if __name__ == '__main__':
    main()

