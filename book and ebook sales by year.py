import matplotlib.pyplot as plt

year = [2008, 2009, 2010, 2011, 2012,2013,2014,2015,2016,2017, 2018, 2019,2020 ]

#Not based on real data; just numbers I came up with for fun
num_book_sales= [700, 500, 300, 480, 250, 800, 840, 900, 820, 600, 650, 700, 720] 
num_ebook_sales = [1000,1500, 1680, 2500, 3000, 3200, 3500, 4200, 5000, 5100, 6600, 6640, 8000] 
plt.plot(year, num_ebook_sales, 'g-', linewidth=2, label='E-books')
plt.plot(year, num_book_sales, 'r--', linewidth=2, label='Books')
plt.xlabel('Year')
plt.ylabel('Number of Sales')
plt.title('Number of Book and E-book sales from 2008 to 2018')
plt.legend()
plt.show()
