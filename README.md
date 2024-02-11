# Cows and Bulls game

<p>Cows and Bulls is a pen and paper code-breaking game usually played between 2 players. In this, a player tries to guess a secret code number chosen by the second player. The rules are as follows:</p>

<ul><li>A player will create a secret code, usually a 4-digit number. &nbsp;This number should have no repeated digits.</li><li>Another player makes a guess (4 digit number) to crack the secret number. Upon making a guess, 2 hints will be provided- Cows and Bulls.</li><li>Bulls indicate the number of correct digits in the correct position and cows indicates the number of correct digits in the wrong position. For example, if the secret code is 1234 and the guessed number is 1246 then we have 2 BULLS (for the exact matches of digits 1 and 2) and 1 COW (for the match of digit 4 in the wrong position)</li><li>The player keeps on guessing until the secret code is cracked. The player who guesses in the minimum number of tries wins.</li></ul>

<p>Let’s see a sample run for better understanding.</p>
<pre>Secret Code: 2345

Guess: 5789
Response: 0 bulls, 1 cow
Guess: 3285
Response: 1 bull, 2 cows
Guess: 6235
Response: 1 bull, 2 cows
Guess: 2435
Response: 2 bulls, 2 cows
Guess: 2685
Response: 2 bulls, 0 cows
Guess: 2345
You guessed right!</pre>
