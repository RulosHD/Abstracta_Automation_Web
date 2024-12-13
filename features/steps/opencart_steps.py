from behave import *
from utils.utils import attach_screenshot

@given(u'ingreso a Portal OpenCart Abstracta')
def step_impl(context):
    try:
        context.opencart_page.ingreso_a_portal("http://opencart.abstracta.us/")
        assert "Your Store" in context.opencart_page.get_text_title()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)
    

@when(u'busco producto en barra de busqueda')
def step_impl(context):
    try:
        context.opencart_page.send_keys_barra_busqueda(context.table.rows[0]['Producto'])
        assert "Search - iPhone" in context.opencart_page.get_text_title_busqueda()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)

@step(u'selecciono el primer registro encontrado')
def step_impl(context):
    try:
        context.opencart_page.click_primer_item()
        assert "iPhone" in context.opencart_page.get_text_title_producto()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)

@step(u'agrego Producto a Carrito de Compra')
def step_impl(context):
    try:
        context.opencart_page.click_boton_agregar_a_carrito()
        assert "iPhone" in context.opencart_page.get_text_label_agregar_producto()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)

@step(u'ingreso a Carrito de Compra')
def step_impl(context):
    try:
        context.opencart_page.click_boton_carrito_compra()
        assert context.opencart_page.is_displayed_carrito_compra()
        context.opencart_page.click_boton_view_cart()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)

@then(u'valido Producto "{producto}" en Carrito de Compra')
def step_impl(context, producto):
    try:
        assert producto in context.opencart_page.get_text_primer_producto_carrito()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)

@step(u'remuevo Producto de Carrito de Compra')
def step_impl(context):
    try:
        context.opencart_page.click_boton_remover_producto()
        assert "Your shopping cart is empty!" in context.opencart_page.get_text_remover_producto()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)

@then(u'valido que producto no exista en Carrito de Compra')
def step_impl(context):
    try:
        assert "Your shopping cart is empty!" in context.opencart_page.get_text_remover_producto()
        attach_screenshot(context.driver)
    except AssertionError as e:
        attach_screenshot(context.driver)
        raise AssertionError(e.message)