# Python Asyncio for Beginners
What is asyncio, how to use it and why use it?

Starting off
## What is Python asyncio
Python asyncio is a concurrent programming design evolving from Python 3.4 to 3.7 and beyond.
It fits in the concurrency ecosystem for slow I/O bound tasks.
Asyncio runs on 1 process, 1 thread and is the most efficient library for concurrency because of requiring just 1 thread.
#### But what is I/O Bound Tasks?
I/O Bound tasks refers to tasks where you might be waiting like fetching 10 images from the internet, 
where improving your CPU won't boost the speed. 
## Why use it?
Consider this example. <br/>
We have a chess champion who is in a chess convention
- They are playing against 24 beginner chess players.
- It takes 5 seconds for this chess champion to make a move. 
- Their opponent takes 55 seconds to make a move. 
- Games end at roughly 60 moves on average (or 30 moves from each side).

#### Synchronous Version
Doing the math, it takes 5+55 = 60 seconds or 1 minute to make a move for each side.
Since we concluded it took 30 move-pairs, it'll take 30 minutes to finish each game.
However since we are playing against 24 opponents, it'll take 30 x 24 = 720 minutes or 12 hours! </br>
Now can we make it quicker? 

####Asynchronous Version
What happens instead is that what we can do is make the chess champion play against 24 players all at once!
Doing the math, it'll take 5 seconds to make a move on each board or 5 x 24 = 120 seconds or 2 minutes to make a move on each board.
Now coming back to the first board, 2 minutes has elapsed and the opponent has more than enough time to make a move, and then we continue from there.
2 minutes x 30 move pairs = 60 minutes or 1 hour! **That's right, we just finished all 24 games in 1 hour, or a 12x improvement!** 
You see the bottleneck here was the fact that the opponent took 55 seconds compared to our chess champion which took a tiny 5 seconds.

## How to use it?
Look at some examples attached and copy the structure. You need boilerplate code like having an async function 
that manages all the asyncio tasks and gather's the result from each of the asyncio tasks.
There's even a script that simulates the chess game I was talking about!

#### Further Reading...
Read [this](https://realpython.com/async-io-python/) article for more depth 

Note: The async-io.py and the non-async-io.py should be looked at before moving on to the chess versions.