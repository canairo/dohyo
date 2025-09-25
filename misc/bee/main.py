import os

class BeeError(Exception):
    pass

class Challenge:
    def __init__(self, limit, target, letters):
        self.limit = limit
        self.target = target
        self.letters = letters
    
    def verify(self, solution):
        try:
            if len(solution) > self.limit:
                raise BeeError("Your solution exceeds the limit.")
            if any([char not in self.letters for char in solution]):
                raise BeeError("Your solution uses disallowed characters.")
            if eval(solution, {}) != self.target:
                raise BeeError(f"Your solution {eval(solution), {}} does not evaluate to the correct answer.")
            print('\n\n\n\n\n')
            return True
        except Exception as e:
            print(e)
            return False

    def __str__(self):
        return f"Your challenge:\nGet to {self.target} using only the characters '{self.letters}'\nYou have {self.limit} characters."

challenges = [
    Challenge(10, 3735928559, '0xabdef'),
    Challenge(50, 10000, "2/"),
    Challenge(15, 4950, "()01aegmnrsu"),
    Challenge(100, "character", '()+014679chr'),
    Challenge(13, "_", '()0[]dir'),
    Challenge(2000, "blunt", "()+-0[]diorst")
]

bees = [r'''
                      __
                     // \
                     \\_/ //
sjw''-.._.-''-.._.. -(||)(')
                    a \'\'\'
''',

r'''
   .--.    W    .--.
 .'    ', {_} ,'    '.
<       =( X )=       >
 '.    .`/\'''\`.    .'
   '--' <XXXXX> '--'
         <XXX>
          <X>  aac
           `
''',


r'''
             . ' ' ' .
            .         .  
            .         .                   __ _  
 .           .       .                    \ _\\_\_/_
    .          ' . '               . .__// // // ._.\
       '  .  .  ' ' .          . '      \\_\\_\\____/
                      ' . . . '          / /   /  \
                        ''',

r'''
              \     /
          \    o ^ o    /
            \ (     ) /
 ____________(%%%%%%%)____________
(     /   /  )%%%%%%%(  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(%%%%%%%)\  \     )
    (__/___/ (%%%%%%%) \___\__)
            /(       )\
          /   (%%%%%)   \
               (%%%)
                 !''',

r'''
     _ ___
     \.\'.\
      \'\'.\
     __\.\:/_//
    {{{{{(__(")
aac `~~~~ >>>^
''',

r'''
 ,-.
 \_/
{|||)<
 / \
 `-^   hjw
'''
]

for i, challenge in enumerate(challenges):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bees[i])
    print("Buzz buzz buzz!")
    print(challenge)
    while not challenge.verify(sol := input("Enter your solution > ")):
        pass
    
from os import urandom
flag = "DOHYO{" + urandom(32).hex() + "}"
