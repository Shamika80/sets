def compare_flight_routes(our_routes, competitor_routes):

  common_destinations = our_routes.intersection(competitor_routes)

  unique_our_routes = our_routes.difference(competitor_routes)

  unique_competitor_routes = competitor_routes.difference(our_routes)

  return common_destinations, unique_our_routes, unique_competitor_routes

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations, unique_our_routes, unique_competitor_routes = compare_flight_routes(our_routes, competitor_routes)

print("Destinations flown by both airlines:", common_destinations)
print("Destinations unique to our airline:", unique_our_routes)
print("Destinations unique to the competitor airline:", unique_competitor_routes)