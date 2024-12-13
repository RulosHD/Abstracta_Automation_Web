from config.init_config import init_config

def before_scenario(context, scenario):
    init_config(context)

def after_scenario(context, scenario):
    print("Cerrando Driver")
    context.driver.quit()