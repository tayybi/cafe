import products
prod_obj = products.Products()

def test_add_product():
    # assembly
    lst = [{2,2},{1,1}]
    # action 
    result = prod_obj.add_product(lst)
    # asserttion
    axpectation = 'list'
    assert axpectation == result



