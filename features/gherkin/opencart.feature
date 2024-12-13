#utf-8
@web @opencart @carritocompra @abstracta
Feature: Funcionalidad carrito de compra OpenCart Abstracta

    Scenario: validar agregar y remover producto en carrito de compra
        Given ingreso a Portal OpenCart Abstracta
        When busco producto en barra de busqueda
            | Producto |
            | iPhone   |
        And selecciono el primer registro encontrado
        And agrego Producto a Carrito de Compra
        And ingreso a Carrito de Compra
        Then valido Producto "iPhone" en Carrito de Compra
        And remuevo Producto de Carrito de Compra
        And valido que producto no exista en Carrito de Compra