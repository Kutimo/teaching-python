survey_responses: list[dict[str, str]] = [
    {'name': 'Alice', 'rating': '5/5', 'comment': '  Excellent service!  '},
    {'name': 'Bob', 'rating': '4/5', 'comment': 'Good experience'},
    {'name': 'Charlie', 'rating': '3/5', 'comment': '  Average  '},
    {'name': 'Diana', 'rating': '5/5', 'comment': 'LOVED IT!!!'}
]


# break down the data

def clean_response(resp):
    return {
        'name': resp['name'],
        'rating': int(resp['rating'][0]),
        'comment': resp['comment'].strip().lower()
    }


cleaned_data = [clean_response(r) for r in survey_responses]

print(survey_responses)

print("--" * 50)

# expected output : Alice: 5* - "excellent service!"
for response in cleaned_data:
    print(
        f"{response['name']}:, {response['rating']}*, {response['comment']} ")
