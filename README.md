# 120-Game-Solver-harder-than-24-Game

In playing the game of 24 points, **I found that someone has proved any given four numbers that between 1 and 24 can be calculated as a multiple of 24.**
 
Inspired by the 24-point game, I created the 120-point game.
Take any 5 positive integers in [1, 120], connect them with the operators +,-,*,/, and (), then calculate the result.

For example, for 1 2 3 4 9, we have 2\*3\*4\*(1+9)=240. For 1 1 3 4 5, we have (1-1)\*3\*4\*5=0. 
we can notice that 240 and 0 are both multiples of 120.

### So the conjecture is, for any such 5 numbers, there must be some combination of operators such that the result of the operation is a multiple of 120.

## This project is to prove the conjecture. I use pypy to calculate almost all cases in 120 game, and finally prove the conjecture is true!
<img width="469" alt="answer" src="https://user-images.githubusercontent.com/119106196/208099079-fb19687e-f80d-42b0-9969-d81c3f3f505f.png">


#### Make sure that you use pypy to run "the120Problem.py", otherwise it will take forever to complete all calculation. 

You can also change some arguments in "the120Problem.py" to calculate some(not all) answers for 120 game.
