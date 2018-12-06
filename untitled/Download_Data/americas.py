import pygal.maps.world as pgl


# pygal.Worldmap()语句相应模块更改为pygal.maps.world。World()
wm = pgl.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
