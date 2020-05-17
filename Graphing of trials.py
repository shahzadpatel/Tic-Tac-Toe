import pandas as pd
import matplotlib.pyplot as plt

# Pie Chart of the User going second at the Easy level
s = pd.Series([54, 6, 4])
s.index = ["Win", "Loss", "Draw"]
s.name = "Going Second"
s.plot(kind='pie', title = 'Easy');
plt.plot(s)
plt.show()

# Pie Chart of the User going first at the Easy level
t = pd.Series([69, 1, 4])
t.index = ["Win", "Loss", "Draw"]
t.name = "Going First"
t.plot(kind='pie', title = 'Easy');
plt.plot(t)
plt.show()

# Pie Chart of the number of Wins, Losses and Draws at the Easy level
u = pd.Series([123, 7, 8])
u.index = ["Win", "Loss", "Draw"]
u.name = "Total Counts"
u.plot(kind='pie', title = 'Easy');
plt.plot(u)
plt.show()

# Pie Chart of the User going second at the Medium level
v = pd.Series([12, 8, 5])
v.index = ["Win", "Loss", "Draw"]
v.name = "Going Second"
v.plot(kind='pie', title = 'Medium');
plt.plot(v)
plt.show()

# Pie Chart of the User going first at the Medium level
w = pd.Series([10, 3, 20])
w.index = ["Win", "Loss", "Draw"]
w.name = "Going First"
w.plot(kind='pie', title = 'Medium');
plt.plot(w)
plt.show()

# Pie Chart of the number of Wins, Losses and Draws at the Medium level
x = pd.Series([22, 11, 25])
x.index = ["Win", "Loss", "Draw"]
x.name = "Total Counts"
x.plot(kind='pie', title = 'Medium');
plt.plot(x)
plt.show()

# Pie Chart of the User going second at the Hard level
y = pd.Series([0, 6, 2])
y.index = ["Win", "Loss", "Draw"]
y.name = "Going Second"
y.plot(kind='pie', title = 'Hard');
plt.plot(y)
plt.show()

# Pie Chart of the User going first at the Hard level
z = pd.Series([5, 10, 18])
z.index = ["Win", "Loss", "Draw"]
z.name = "Going First"
z.plot(kind='pie', title = 'Hard');
plt.plot(z)
plt.show()

# Pie Chart of the number of Wins, Losses and Draws at the Hard level
a = pd.Series([5, 16, 20])
a.index = ["Win", "Loss", "Draw"]
a.name = "Total Counts"
a.plot(kind='pie', title = 'Hard');
plt.plot(a)
plt.show()