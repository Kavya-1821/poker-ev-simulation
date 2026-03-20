import random

#Create a standard deck of 52 cards
suits = ['H','S','D','C']
ranks = list(range(2,15)) #11,12,13,14 assigned for K,Q,J,A respectively
deck = [(rank, suit) for rank in ranks for suit in suits]

#Randomly deal the required number of cards from the deck
def deal_cards(deck, num_cards):
    return random.sample(deck, num_cards)

#Define hand strength using the highest card in the hand
def hand_strength(hand):
    return max(card[0] for card in hand)

#Simlaute one game between player and opponent
def simulate_game():
    deck_copy = deck.copy()

    #Deal 2 cards to each player
    player_hand = deal_cards(deck_copy, 2)
    opponent_hand = deal_cards(deck_copy, 2)

    #Compute respective hand strengths
    player_strength = hand_strength(player_hand)
    opponent_strength = hand_strength(opponent_hand)

    #Return game outcome
    if player_strength > opponent_strength:
        return 1
    elif player_strength < opponent_strength:
        return -1
    else:
        return 0

#Run repeated simulations and count outcomes
def run_simulation(num_trials=100000):
    wins = 0
    ties = 0
    losses = 0
    
    for _ in range(num_trials):
        result = simulate_game()

        if result == 1:
            wins+= 1
        elif result == -1:
            losses += 1
        else: 
            ties += 1

    return wins, losses, ties

#Compute win probability and expected value
def calculate_results(wins, losses, ties, total):
    win_probability = wins/total
    loss_probability = losses/total

    #Expected value = (+1)*P(win) + (-1)*P(loss)
    expected_value = (win_probability * 1) + (loss_probability * -1)
    return win_probability, expected_value

def main():
    num_trials = 100000
    print("Running simulation")

    #Run Monte Carlo trials
    wins, losses, ties = run_simulation(num_trials)
    win_probability, expected_value = calculate_results(wins, losses, ties, num_trials)
    
    #Calculate probability and EV from simulation outcomes
    print("\nResults :")
    print(f"Total Games: {num_trials}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")
    print(f"\nWin Probability: {win_probability:.4f}")
    print(f"Expected Value: {expected_value:.4f}")

if __name__ == "__main__":
    main()