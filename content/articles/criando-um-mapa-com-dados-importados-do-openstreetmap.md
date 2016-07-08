Title: Criando um mapa com dados importados do OpenStreetMap
Date: 2013-11-06 23:38
Author: admin
Category: software.livre, tech, tutoriais
Tags: geojson, mapas, openstreetmap, tutoriais
Slug: criando-um-mapa-com-dados-importados-do-openstreetmap
Status: published

Eu mapeei todas as estações de compartilhamento de bicicletas do
BikeSalvador e queria fazer um mapa que mostrasse essas estações. Quando
havia apenas cinco estações, após mapear no OSM, eu criei um arquivo
GeoJSON usando o [geojson.io](http://geojson.io). Porém agora já são 19
estações. Seria um retrabalho enorme mapear as estações no OSM e depois
criar o geojson manualmente.

Felizmente conheci o osmfilter, um software para filtrar os dados do
[OpenStreetMap](http://osm.org). Combinando o osmfilter com o geojson.io
é possível facilmente extrair alguns dados do OpenStreetMap e apresentar
essa informação em um mapa personalizado. Então vamos às instruções de
como fazer isso.

O primeiro passo é baixar os dados do OSM. Se você quiser trabalhar com
a base de dados de todo o Brasil, você pode baixar dos servidores do
[GeoFabrik](http://download.geofabrik.de). Como eu necessitava apenas
dos dados de uma cidade, utilizei o editor
[JOSM](http://josm.openstreetmap.de/), fiz o download dos dados e salvei
em um arquivo .osm no meu computador.

![Download dos dados no
JOSM](http://images.wille.blog.br/josm.jpg)

Agora nós precisamos utilizar o osmfilter. Veja as instruções de
instalação na página [osmfilter no Wiki do
OpenStreetMap](https://wiki.openstreetmap.org/wiki/Osmfilter). O comando
que eu utilizei para filtrar as estações de compartilhamento de
bicicletas de Salvador foi:

`./osmfilter salvador.osm --keep="amenity=bicycle_rental" > bikesalvador.osm`

Você pode combinar mais de um filtro em um único comando. Por exemplo,
se você quiser filtrar todos os restaurantes italianos, você poderia
utilizar `--keep="amenity=restaurant and cuisine=italian"`.

Aqui entra o [geojson.io](http://geojson.io). Acesse o site, clique no
botão Open e importe o arquivo gerado pelo osmfilter.

![geojson.io
interface](http://images.wille.blog.br/geojson-open.jpg)

Após isso, você vai ver todos os dados filtrados sobre o mapa, inclusive
os metadados. Se parte dos metadados não te interessar, você pode
remover uma ou mais colunas.

Você vai precisar de uma conta no [GitHub](http://github.com) para
salvar seu arquivo GeoJSON. Depois de salvar, o GitHub irá te fornecer
uma [página com o seu
GeoJSON](https://gist.github.com/willemarcel/37a8be9409baa07cf31e) e
também um código para que você possa incluir o mapa que você criou em
uma página web. O mapa gerado pelo geojson.io é esse abaixo:

<p>
<script src="https://gist.github.com/willemarcel/37a8be9409baa07cf31e.js"></script>
</p>
Quem quiser criar um mapa ainda melhor, recomendo ler esse [tutorial de
como adicionar uma camada GeoJSON ao
Leaflet](http://lyzidiamond.com/posts/osgeo-august-meeting/).
