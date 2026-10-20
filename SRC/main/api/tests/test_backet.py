from playwright.sync_api import expect



def test_add_item_and_chec_in_cart(page,auth_standard_user):
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    product1 = page.locator('.inventory_item', has_text='Sauce Labs Fleece Jacket')
    product1_name = product1.locator('.inventory_item_name').inner_text()
    product1_price = product1.locator('.inventory_item_price').inner_text()
    buton1 = product1.locator('button').click()
    product2 = page.locator('.inventory_item', has_text='Sauce Labs Bolt T-Shirt')
    product2_name = product2.locator('.inventory_item_name').inner_text()
    product2_price = product2.locator('.inventory_item_price').inner_text()
    buton2 = product2.locator('button').click()


    assert page.locator('[data-test="shopping-cart-badge"]').inner_text() == '2'

    cart = page.locator('[data-test="shopping-cart-link"]').click()

    expect(page).to_have_url('https://www.saucedemo.com/cart.html')

    name1_cart = page.locator('[data-test="inventory-item-name"]', has_text='Sauce Labs Fleece Jacket')
    name2_cart = page.locator('[data-test="inventory-item-name"]', has_text='Sauce Labs Bolt T-Shirt')

    assert name1_cart.inner_text() == "Sauce Labs Fleece Jacket"
    assert name2_cart.inner_text() == "Sauce Labs Bolt T-Shirt"

def test_remove_item_from_cart(page,auth_standard_user):
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    product = page.locator('.inventory_item', has_text='Sauce Labs Backpack')
    product.locator('button').click()
    product1 = page.locator('.inventory_item', has_text='Test.allTheThings() T-Shirt (Red)')
    product1.locator('button').click()

    cart = page.locator('[data-test="shopping-cart-link"]').click()

    expect(page).to_have_url('https://www.saucedemo.com/cart.html')

    expect(page.locator('[data-test="inventory-item-name"]', has_text='Sauce Labs Backpack')).to_have_text('Sauce Labs Backpack')
    expect(page.locator('[data-test="inventory-item-name"]', has_text='Test.allTheThings() T-Shirt (Red)')).to_have_text('Test.allTheThings() T-Shirt (Red)')

    page.locator('[data-test="remove-test.allthethings()-t-shirt-(red)"]').click()
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()
    expect(page.get_by_text('Remove')).not_to_be_visible()



