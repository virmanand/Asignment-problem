# # Python script to generate a personalized greeting message

# def generate_greeting(first_name, last_name):
#     """
#     Generate a personalized greeting message for a person using their first and last names.

#     Args:
#         first_name (str): The person's first name.
#         last_name (str): The person's last name.

#     Returns:
#         str: A personalized greeting message.
#     """
#     greeting_message = f"Hello, {first_name} {last_name}! It's nice to meet you."
#     return greeting_message

# # Get the user's first and last names
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # Generate and display the personalized greeting message
# greeting_message = generate_greeting(first_name, last_name)
# print(greeting_message)
# Python script to find the runner-up score in a sports competition

def find_runner_up(scores):
    """
    Find the runner-up score in a sports competition.

    Args:
        scores (list): A list of scores.

    Returns:
        int: The runner-up score.
    """
    # Check if the list of scores is empty
    if not scores:
        return None

    # Sort the scores in descending order
    scores.sort(reverse=True)

    # The runner-up score is the second highest score
    runner_up_score = scores[1]

    return runner_up_score

# Example usage:
scores = [85, 90, 78, 92, 88, 76, 95, 89]
runner_up_score = find_runner_up(scores)

if runner_up_score is not None:
    print(f"The runner-up score is: {runner_up_score}")
else:
    print("No scores available.")