from falsy.falsy import FALSY

f = FALSY(static_path='test', static_dir='demo/simple/static',log_config={'highlights':['falsy']})
f.swagger('demo/simple/spec.yml', ui=True, ui_language='zh-cn', theme='bootstrap')
api = f.api
