from djbitcoin.utils import is_bitcoin_address_valid


def test_is_bitcoin_address_valid():
    assert is_bitcoin_address_valid('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2')
    assert is_bitcoin_address_valid('3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy')
    assert not is_bitcoin_address_valid('3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLx')
    assert not is_bitcoin_address_valid('1234')
    assert not is_bitcoin_address_valid('2MwtpivYqrwzfbSxCjHEWpVrRS6U0MACJ1i0')
