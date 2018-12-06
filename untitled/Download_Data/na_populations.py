import pygal.maps.world as pgl


# pygal.Worldmap()语句相应模块更改为pygal.maps.world.World()
wm = pgl.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'max': 113423000})

wm.render_to_file('na_populations.svg')
