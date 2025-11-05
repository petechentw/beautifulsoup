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


```
python3 -m bs4.tests.test_milestone3
```

```
python3 -m apps.m3.task7 apps/m3/input.html
```