# Find Most Starred Repositories Using GitHub API for Specific Languages

import requests # used to send HTTP requests to API

# GitHub API URL to search repositories
GITHUB_API_URL = "https://api.github.com/search/repositories"


# Function to create search query
# min_stars has default value 60000
def create_query(languages, min_stars=60000):
    
    # Start query with minimum stars condition
    query = f"stars:>{min_stars} "
    
    # Add languages to query
    for language in languages:
        query += f"language:{language} "
        
    # A sample query looks like: "stars:>50 language:python language:javascript"
    return query


# Function to fetch repositories from GitHub API
def repos_with_most_stars(languages, sort="stars", order="desc"):
    
    # Create search query
    query = create_query(languages)
    
    # Parameters to send with API request
    params = {
        "q": query,     # search query
        "sort": sort,   # sort by stars
        "order": order  # descending order
    }
    
    # Send GET request to GitHub API
    response = requests.get(GITHUB_API_URL, params=params)
    
    # Get HTTP status code (200 = success)
    status_code = response.status_code
    
    # Check if request succeeded or failed
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
    else:
        # Convert response to JSON (Python dictionary)
        response_json = response.json()
        
        # Return list of repositories
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