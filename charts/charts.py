import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Sample Pie Chart')
    plt.savefig('pie_chart.png')
    plt.close()
    