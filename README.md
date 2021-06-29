# Random Python hackerrank problems in one line
- No semi-colons, No gimmicks, just lambdas and state manipulation. 
- So before you go shouting over the roof, some programs aren't one-liners cause hackerrank doesn't allow me to remove the boiler-plate code for getting the input. but yeah it's just an extra lambda to get and throw the input into the function to make it one line.

### why am I wasting my time like this?
- why not? , just for the funzies
- I don't understand what I write, but hey it's rewarding when it all comes together in a single line.

### Bonus
- All programs in python can be converted to a single line if u eval the decoded base64 version of the source-code
- All the above programms are originally written by me, when I was bored.
- As a timestamp , I started this challenge on 9th Jun 2021.

### Snippets that were helpful from the internet

This one's from python discord guild, y'all are awesome (slightly edited to work with py 3.7 cause hackerrank uses that)
```py
try_ = lambda t, *a, f=lambda a:a, e=Exception, **k,:([r for globals()["r"] in [{}]][0]).pop(
    'r',
    type(
        '',
        (__import__('contextlib').ContextDecorator,),
        {
            '__enter__':int,
            '__exit__':lambda s,*a:isinstance(
                a[1], e
            ) and [r.update(
                r=f(a)
            )]
        }
    )()(t)(*a, **k)
)
try_(lambda:1/0,f=lambda *a:print('wat'),e=ZeroDivisionError)
```

Minified
```py
(lambda t, *a, f=lambda a:a, e=Exception, **k,:([r for globals()["r"] in [{}]][0]).pop('r',type('',(__import__('contextlib').ContextDecorator,),{'__enter__':int,'__exit__':lambda s,*a:isinstance(a[1], e) and [r.update(r=f(a))]})()(t)(*a, **k)))
 ```