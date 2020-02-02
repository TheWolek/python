print(f'Invoking __init__.py for {__name__}')
import package.mod1 as mod1, package.mod2 as mod2
mod1.__init__()
mod2.__init__()