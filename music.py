def compile_unique_lineup(artist_names):
 
  unique_artists = set()
  duplicate_found = False  

  for artist in artist_names:
    if artist in unique_artists:
      duplicate_found = True
      break  
    unique_artists.add(artist)

  return unique_artists, duplicate_found

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

unique_artists, duplicate_found = compile_unique_lineup(artist_names)

if duplicate_found:
  print("Duplicate artists found in the list!")
else:
  print("No duplicate artists found.")

print("Unique artist lineup:", unique_artists)