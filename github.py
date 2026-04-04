import requests

# API URL for GITHUB repositories
GITHUB_API_URL = "https://api.github.com/search/repositories"

# If no value is passed, 60000 is used by default
def create_query(languages, min_stars=60000):
    query = f"stars:>{min_stars} "
    
    for language in languages:
        query += f"language:{language} "
        
        # a sample query looks like: "stars:>50 language:python language:javascript"
        return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}     # send parameters to API
    
    response = requests.get(GITHUB_API_URL, params=params)  # fetch data from API
    status_code = response.status_code
    
    # Check if request succeeded or failed
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
    else:
        response_json = response.json()     # convert API response into python dictionary
        return response_json["items"]

# Main program execution starts here
if __name__ == "__main__":
    
    # List of languages to search
    languages = ["python", "javascript", "ruby"]
    
    # Fetch repositories
    results = repos_with_most_stars(languages)
    
    # Loop through results and print information
    for result in results:
        language = result["language"]           # repository language
        stars = result["stargazers_count"]      # star count
        name = result["name"]                   # repository name
        
        # Print formatted output
        print(f"-> {name} is a {language} repo with {stars} stars.")