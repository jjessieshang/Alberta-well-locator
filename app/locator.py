from app import app
import folium

@app.route('/mapping/')
def mapping():

    # Implementing Folium Map
    m = folium.Map(location=[55,-115], tiles =None,
                    zoom_start=5)

    # map tiles - light, satellite, topography, alberta geoJson
    borderStyle={
        'fillOpacity': 0.1,
        'weight': 1,
        'color': 'black'
    }

    folium.GeoJson("alberta.geojson", 
                    name="Alberta",
                    style_function=lambda x:borderStyle).add_to(m)
    folium.TileLayer("https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png", 
                 name = 'Light Map',
                 attr= 'Stadia Maps').add_to(m)
    folium.TileLayer('https://api.maptiler.com/maps/outdoor/{z}/{x}/{y}.png?key=D1R440GkNxYWsQt9rTf3', 
                 name = 'Topography',
                 attr= 'OpenTopo').add_to(m)
    folium.TileLayer('https://api.maptiler.com/maps/hybrid/256/{z}/{x}/{y}.jpg?key=D1R440GkNxYWsQt9rTf3', 
                 name = 'Satellite',
                 attr= 'Esri_WorldImagery').add_to(m)
    folium.LayerControl().add_to(m)

    return m._repr_html_()

