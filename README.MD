# The Optom Automator

_Find yourself saying 1 or 2 a little too much? Then, this tool is for you._

This is a fun hobby project that I have been working on, where the main purpose is to repeat phrases that I commonly say in an eye examination.

It's still a work in progress...

## The Phrase Tree

How this works?

There is a sequence to the phrases. I call it a 'phrase tree'. The phrase tree is divced into 'stages'.

1. GREETING
2. HISTORY
3. RIGHT_VA
4. LEFT_VA
5. RIGHT_REDGREEN
6. RIGHT_CYLINDER
7. RIGHT_SPHERE
8. LEFT_REDGREEN
9. LEFT_CYLINDER
10. LEFT_SPHERE
11. END_EXAM

The capitals represent the 'stages' of the testing. They can act as keys for tuples. The tuples provide a little variation in testing.

The tuples phrases can be played in sequence or at random.

This is how the dictionary is constructed roughly:

```python
_PHRASES = {
    "STAGE_1": ("random", ("choice1", "choice2")),
    "STAGE_2": ("sequence", ("choice1", "choice2")),
}
```
