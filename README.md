# Family Location
## Installation

```bash
pip install folium
pip install geopy
```
Python version: 3.9.2
<br>

---

## Usage
```python
class App:
    def __init__(self):
        self.__url = #CHANGE THIS
        self.__display = Display(self.__url)
        self.run()
```
All you need to do is download a FamilyScript file of a family tree and set the url to the url property of the main app class. <br>
Changing this url to your own file will produce the map for your family tree.
<br>
You will need to wait for n = ((number of members of family tree) + ~1) seconds, after which an HTML document will be returned to the main directory. <br>
Opening this HTML file in your chosen web browser will show the map.


---
## Dependencies:
 - Python 3.9.2 (Any version 3+ should work)
 - geopy 2.2.0
 - folium 0.12.1
 - leaflet.js 1.9
 - jinja2 3.1.2
 - requests (default)
 - webbrowser (default)
 - branca 0.5.0
