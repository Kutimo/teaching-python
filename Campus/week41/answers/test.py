survey_responses: List[Dict[str, str]] = [
    {'name': 'Alice', 'rating': '5/5', 'comment': '  Excellent service!  '},
    {'name': 'Bob', 'rating': '4/5', 'comment': 'Good experience'},
    {'name': 'Charlie', 'rating': '3/5', 'comment': '  Average  '},
    {'name': 'Diana', 'rating': '5/5', 'comment': 'LOVED IT!!!'}
]

# Lambda function to clean and normalize each response


def clean_response(resp): return {
    'name': resp['name'],
    'rating': int(resp['rating'].split('/')[0]),  # Convert "5/5" to 5
    # Clean whitespace and lowercase
    'comment': resp['comment'].strip().lower()
}


# List comprehension to process all survey responses
cleaned_data = [clean_response(r) for r in survey_responses]

print("Example 2: Cleaned Survey Responses")
print("-" * 50)
for response in cleaned_data:
    print(
        f"{response['name']}: {response['rating']}* - \"{response['comment']}\"")
