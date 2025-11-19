# Milestone-3

It now supports three optional transformer functions:

- Changes the tag name

```
name_xformer(tag) 
```
- Modifies tag attributes

```
attrs_xformer(tag) 
```

- Performs side effects directly on the tag

```
xformer(tag) 
```


### Test
```
cd bs4/tests 
```

```
python3 -m pytest -q test_milestone3.py
```


-----------------------------------
```
python3 -m apps.m3.task7 apps/m3/input.html
```