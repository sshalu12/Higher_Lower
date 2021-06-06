from art import logo,vs
from game_data import data
import random
from replit import clear

def display():
  print(f"Compare A: {A['name']} ,a {A['description']}, from {A['country']}. ")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
  
  #print(A['follower_count'])
  #print(B['follower_count'])

print(logo)
end_game=True
score=0
A=random.choice(data)
while end_game:
  B=random.choice(data)
  while A==B:
    B=random.choice(data)
  display()
  choice=input("\nWho has more followers? Type 'A' or 'B': ").lower()
  
  if (A['follower_count']>B['follower_count'] and choice=="a") or (B['follower_count']>A['follower_count'] and choice=="b") :
    score +=1
    clear()
    print(logo)
    print(f"You're Right! current score: {score}.")
    A=B
  
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    end_game=False

