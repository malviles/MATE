import folium

mapa = folium.Map(location=[19.7229436, -101.188395], zoom_start=25)


folium.Marker([19.7229436, -101.188395], popup='Mi Marcador').add_to(mapa)

mapa.save('mapa_sin_internet.html')
