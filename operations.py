
def remove_duplicates_set(customer_ids):

  unique_customer_ids = set(customer_ids)

  return unique_customer_ids

def remove_duplicates_loop(customer_ids):
 
  unique_customer_ids = []

  for id in customer_ids:
    if id not in unique_customer_ids:
      unique_customer_ids.append(id)

  return unique_customer_ids

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_ids_set = remove_duplicates_set(customer_ids)
print("Unique Customer IDs (using set):", unique_ids_set)

unique_ids_loop = remove_duplicates_loop(customer_ids)
print("Unique Customer IDs (using loop):", unique_ids_loop)