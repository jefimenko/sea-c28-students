from lambda_magic import function_builder

def test_has_lambdas():
    l = function_builder(10)
    
    for order, func in enumerate(l):
        assert func(5) == 5 + order

def test_zero_case():
    l = function_builder(0)
    
    assert l == []

def test_negative_case():
    l = function_builder(-10)
    
    assert l == []
