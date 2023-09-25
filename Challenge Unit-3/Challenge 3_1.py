def linearSearchProduct(productList, targetProduct): 
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

# Example usage:

products = ['ball pen','gel pen','ink pen','gel pen']
target = 'gel pen'
target2 = 'apple'
result = linearSearchProduct(products, target) 
print(result)