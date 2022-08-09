# Spartan Five Letter Words

As proven by Zach Snyder, *300 is enough*.

The 300 bytes in `s.py` solve Matt Parker's Five Letter Words problem in 4 minutes.

It is a depth-first-search with pruning based on anagram bitmasks of the words instead of the words themselves, committing several Python war crimes on the way.

# Usage

You need Python 3.

Get `words_alpha.txt` from here: https://github.com/dwyl/english-words and put it into this folder.

Run it from the terminal:

```sh
python3 s.py < words_alpha.txt
```

# Less takes More

Though if you have a month to spend, like some people, `t.py` can get to the solution with only *199 bytes* in a week or so.

```sh
python3 t.py < words_alpha.txt
```
