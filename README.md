# mastermind
Mastermind game simulator and solver.

  1. To learn how to play Mastermind board game and its variants: https://en.wikipedia.org/wiki/Mastermind_(board_game)
  2. To simulate the entire game (let the computer be both the codemaker and codebreaker):
     
     python mastermind_simulator.py both
     
     sample output:
     
      code maker set to: ['green', 'blue', 'green', 'white']
      
      code breaker start cracking:
      
      attempt 1: ['red', 'blue', 'green', 'white'], key pegs: {'black': 3, 'white': 0}
      
      attempt 2: ['red', 'blue', 'green', 'red'], key pegs: {'black': 2, 'white': 0}
      
      attempt 3: ['red', 'white', 'green', 'white'], key pegs: {'black': 2, 'white': 0}
      
      attempt 4: ['red', 'blue', 'yellow', 'white'], key pegs: {'black': 2, 'white': 0}
      
      attempt 5: ['black', 'blue', 'green', 'white'], key pegs: {'black': 3, 'white': 0}
      
      attempt 6: ['blue', 'blue', 'green', 'white'], key pegs: {'black': 3, 'white': 0}
      
      attempt 7: ['green', 'blue', 'green', 'white'], key pegs: {'black': 4, 'white': 0}
      
      solution reached after 7th attempt
      
    3. To simulate the codebreaker only (require user input):

     python mastermind_simulator.py breaker
     
     attempt 1: ['red', 'white', 'white', 'green']
     num of black pegs:2 
     num of white pegs:1
     attempt 2: ['white', 'green', 'white', 'green']
     ...
     
     
     
     
     
