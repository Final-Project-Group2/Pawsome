

def two_val(data):
      D = dict()
      for k,v in data.items():
            D[k], options=None, None
            if issubclass(tuple, v[0].__class__) :
                  options = [(i[0], i[1][0]) if  issubclass( list,i[1].__class__) else (i[:2]) for i in v  ] 
            elif issubclass(dict,v[0].__class__):
                  options = dict()
                  for d in v:
                        key=d['name']
                        iterable = d["value"]
                        options[key] = list(tuple(x[:2]) for x  in iterable )
            D[k] = options
      return D