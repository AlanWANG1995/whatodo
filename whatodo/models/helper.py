
def before(pre_fn):
  def wrapper(fn):
    def _fn(*arg, **kwarg):
      pre_fn(*arg, **kwarg)
      return fn(*arg, **kwarg)
    return _fn
  return wrapper

def after(aft_fn):
  def wrapper(fn):
    def _fn(*arg, **kwarg):
      v = fn(*arg, **kwarg)
      aft_fn(*arg, **kwarg)
      return v
    return _fn
  return wrapper



