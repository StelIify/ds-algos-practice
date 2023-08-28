class WeightedGraphVertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}

    def add_adjacent_vertex(self, vertex, weigh):
        self.adjacent_vertices[vertex] = weigh


class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def __repr__(self):
        return self.name

    def add_route(self, city, price):
        self.routes[city] = price


def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}
    unvisited_cities = set()
    visited_cities = {}

    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city

    while current_city:
        visited_cities[current_city.name] = True
        if current_city in unvisited_cities:
            unvisited_cities.remove(current_city)

        for adjacent_city, price in current_city.routes.items():
            if not visited_cities.get(adjacent_city.name):
                unvisited_cities.add(adjacent_city)

            price_through_current_city = cheapest_prices_table[current_city.name] + price

            if not cheapest_prices_table.get(adjacent_city.name) or \
                    price_through_current_city < cheapest_prices_table[adjacent_city.name]:
                cheapest_prices_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name

        current_city = min(unvisited_cities, key=lambda city: cheapest_prices_table[city.name], default=None)

    shortest_path = []
    current_city_name = final_destination.name

    while current_city_name != starting_city.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]
    shortest_path.append(starting_city.name)

    return shortest_path[::-1]


def dijkstra_practice(start, finish):
    cheapest_price = {}
    cheapest_stopover_city = {}
    unvisited_cities = set()
    visited_cities = {}

    current_city = start
    cheapest_price[current_city.name] = 0

    while current_city:
        visited_cities[current_city] = True
        if current_city in unvisited_cities:
            unvisited_cities.remove(current_city)
        for route, price in current_city.routes.items():
            if not visited_cities.get(route):
                unvisited_cities.add(route)
            price_through_city = cheapest_price[current_city.name] + price
            if not cheapest_price.get(route.name) or price_through_city < cheapest_price[route.name]:
                cheapest_price[route.name] = price_through_city
                cheapest_stopover_city[route.name] = current_city.name
        min_route = float("inf")
        current_city = None
        for city in unvisited_cities:
            if cheapest_price[city.name] < min_route:
                min_route = cheapest_price[city.name]
                current_city = city

    shortest_path = []
    current_city_name = finish.name
    while current_city_name != start.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_stopover_city[current_city_name]
    shortest_path.append(start)

    return shortest_path[::-1]


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

path = dijkstra_practice(atlanta, el_paso)
print(path)
