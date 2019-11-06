### Function: Retreiving name of a variable

```python
import inspect
def varname(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
```

* Usage
```python
def chk_10(arr):
    chk = 0
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < 10:
            print('in {}, index={}, value={}'.format(retrieve_name(arr), i, arr[i]))
            chk += 1
    print('in {}, total {} points error.'.format(retrieve_name(arr), chk))

chk_10(seq0)
```
```
in seq0, total 0 points error.
```
