import streamlit as st
import random

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():

    if 'user_score' not in st.session_state:
        st.session_state.user_score = 0
    if 'computer_score' not in st.session_state:
        st.session_state.computer_score = 0
    if 'user_consecutive_wins' not in st.session_state:
        st.session_state.user_consecutive_wins = 0
    if 'computer_consecutive_wins' not in st.session_state:
        st.session_state.computer_consecutive_wins = 0

    st.title("Rock-Paper-Scissors Game")

    # Play the game until user decides to stop
    play_again = True
    while play_again:
        # Input field with styling
        user_choice = st.radio("Choose your weapon:", ['Rock', 'Paper', 'Scissors'])

        # Generate computer's choice
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

        # Display computer's choice
        st.write(f"Computer chooses: {computer_choice}")

        # Determine winner and display result
        result = determine_winner(user_choice, computer_choice)
        st.success(result)

        # Update scores and consecutive win counters
        if result == "You win!":
            st.session_state.user_score += 1
            st.session_state.user_consecutive_wins += 1
            st.session_state.computer_consecutive_wins = 0
        elif result == "Computer wins!":
            st.session_state.computer_score += 1
            st.session_state.computer_consecutive_wins += 1
            st.session_state.user_consecutive_wins = 0
        else:
            st.session_state.user_consecutive_wins = 0
            st.session_state.computer_consecutive_wins = 0

        # Display scores
        st.write(f"Your score: {st.session_state.user_score}")
        st.write(f"Computer's score: {st.session_state.computer_score}")

        # Check for consecutive wins and add bonus points
        if st.session_state.user_consecutive_wins >= 2:
            st.session_state.user_score += 1
            st.write("Bonus point! You've won two consecutive times!")
            st.session_state.user_consecutive_wins = 0
        elif st.session_state.computer_consecutive_wins >= 2:
            st.session_state.computer_score += 1
            st.write("Bonus point! Computer has won two consecutive times!")
            st.session_state.computer_consecutive_wins = 0

        # Ask user to play again
        play_again = st.button("Play Again?")

        # Add a separator between rounds
        st.markdown("---")

    # Add a footer
    st.markdown("---")

if __name__ == "__main__":
    main()
