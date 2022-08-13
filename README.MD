# The Optom Automator

_Find yourself saying 1 or 2 a little too much? Then, this tool is for you._

This is a fun hobby project that I have been working on, where the main purpose is to repeat phrases that I commonly say in an eye examination.

## Phrases

How this works?

There is a usual sequence (for refraction). And that is:
    1. (intro)
      a. GREETING ->
      b. HISTORY ->
    2. (preliminary)
      a. RIGHT_VA ->
      b. LEFT_VA ->
    3. (refraction)
      a. RIGHT_REDGREEN ->
      b. RIGHT_CYLINDER ->
      c. RIGHT_SPHERE ->
      d. LEFT_SPHERE(R/G) ->
      e. LEFT_CYLINDER ->
      f. LEFT_SPHERE(FINE) ->
    4. (end)
      END_EXAM -|

The capitals represent the 'stages' of the testing. They can act as keys for tuples. The tuples provide a little variation in testing.

The tuples phrases can be played in sequence or at random.

This is how the dictionary is constructed roughly:

```python
_PHRASES = {
    "STAGE_1": ("random", ("choice1", "choice2")),
    "STAGE_2": ("sequence", ("choice1", "choice2")),
}
```
