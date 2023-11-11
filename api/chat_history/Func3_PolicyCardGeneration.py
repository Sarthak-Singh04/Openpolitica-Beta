import requests
import json
from apikey import apikey

def generate_policy_card(user_needs_rankings, openai_api_key):
    """
    Generate a policy card based on user needs using GPT.

    Args:
    user_needs_rankings (dict): A dictionary of user needs and their rankings.
    openai_api_key (str): Your OpenAI API key.

    Returns:
    dict: A policy card with policy recommendations.
    """

    # Prepare the prompt for the GPT model
    prompt = "Generate policy recommendations for the following user needs:\n"
    for need, ranking in user_needs_rankings.items():
        prompt += f"- {need} (Ranking: {ranking})\n"

    # API request to OpenAI
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "text-davinci-003",  # or any other suitable model
        "prompt": prompt,
        "max_tokens": 500  # Adjust as needed
    }

    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
    response_data = response.json()

    # Extract the policy recommendations from the response
    policy_recommendations = response_data.get('choices', [{}])[0].get('text', '').strip()

    # Build the policy card
    policy_card = {
        "policy_card_prompt": "Policy for addressing user needs",
        "policy_card_description": "Generated policies to address user needs.",
        "policy_recommendations": policy_recommendations,
        "policy_category": "Urban Development"  # Example category
    }

    return policy_card

# Example usage
user_needs = {
    "Affordability of food in local area": 5,
    "Safety of local area": 3,
    "Affordability of college": 4
}

openai_api_key = apikey  # Replace with your actual OpenAI API key
policy_card = generate_policy_card(user_needs, openai_api_key)
print(json.dumps(policy_card, indent=2))