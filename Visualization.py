import null as null
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# %matplotlib inline

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())

'''fig, ax = plt.subplots()

# --------------------------------------------------------------Task 1
# scatter the sepal_length against the sepal_width

ax.scatter(titanic['fare'], titanic['age'])
# set a title and labels
ax.set_title('pearsonr=0.096, p=0.01')
ax.set_xlabel('fare')
ax.set_ylabel('age')
# colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}

# titanic.plot.hist(subplots=True, layout=(0,0), figsize=(10, 10), bins=20)
plt.show()

# --------------------------------------------------------------Task 2
x = titanic['fare']
num_bins = 30
n, bins, patches = plt.hist(x, num_bins, facecolor='red', alpha=0.5)
plt.xlabel('fare')
plt.xlim(0, 500)
plt.ylim(0, 500)
plt.grid(True)
plt.show()'''

sns.jointplot(x='fare', y='age', data=titanic)
plt.show()
sns.distplot(titanic['fare'], bins=30, kde=False, color='RED')
plt.show()
plt.ylim(0, 80)
# df = titanic[(titanic['age'] < 100) | (titanic['age'] > 80)]
df = titanic[(titanic['age']) >= 100]
sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')
plt.show()
plt.ylim(top=90)
plt.ylim(bottom=-10)

ax = sns.swarmplot(x='class', y='age', data=titanic, palette='rainbow')
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
plt.show()

sns.countplot(x='sex', data=titanic)
plt.ylim(top=600)
plt.show()

sns.heatmap(titanic.corr(), robust=True, fmt="f", vmin=-1.0, vmax=1.0, cbar_kws={'ticks': [-0.8, -0.4, 0, 0.4, 0.8]})
plt.title('titanic.corr()')
plt.show()

g = sns.FacetGrid(titanic, col='sex')
g = g.map(plt.hist, 'age')
g = plt.xlim(left = 0)
plt.show()
