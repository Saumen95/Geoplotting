from mpl_toolkits import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill', llcrnrlat=20, ucrnrlat=50, /
            llcrnrlon=-130, ucrnrlon=-60, resolution='c')

m.drawcoastline()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')

lat = 30, 31, 33, 34, 38
lon = -103, -110, -111, -150, -92

lat2 = 35, 43, 33, 54, 38
lon2 = -107, -115, -111, -150, -88

x, y = m(lon, lat)
m.plot(x, y, 'ro', markersize=20, alpha=.5)

x, y = m(lon2, lat2)
m.plot(x, y, 'go', markersize=20, alpha=.5)

plt.title('Geo plotting')
plt.show()
