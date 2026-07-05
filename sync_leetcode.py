import os
import requests

SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")

if not SESSION or not CSRF_TOKEN:
    print("Error: Missing LeetCode session or CSRF token secrets.")
    exit(1)

URL = "https://leetcode.com"
HEADERS = {
    "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF_TOKEN}",
    "X-CSRFToken": CSRF_TOKEN,
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json"
}

LIST_QUERY = """
query userRecentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    titleSlug
    lang
  }
}
"""

CODE_QUERY = """
query submissionDetails($submissionId: ID!) {
  submissionDetails(submissionId: $submissionId) {
    code
  }
}
"""

EXTENSIONS = {
    "python3": "py", "python": "py", "javascript": "js", "typescript": "ts", 
    "cpp": "cpp", "java": "java", "golang": "go", "csharp": "cs", "ruby": "rb"
}

def get_username():
    query = "query { user { username } }"
    res = requests.post(URL, json={"query": query}, headers=HEADERS).json()
    return res["data"]["user"]["username"]

def main():
    username = get_username()
    payload = {"query": LIST_QUERY, "variables": {"username": username, "limit": 20}}
    response = requests.post(URL, json=payload, headers=HEADERS).json()
    submissions = response["data"]["recentAcSubmissionList"]
    
    os.makedirs("solutions", exist_ok=True)
    
    for sub in submissions:
        sub_id = sub["id"]
        slug = sub["titleSlug"]
        lang = sub["lang"]
        ext = EXTENSIONS.get(lang, "txt")
        filename = f"solutions/{slug}.{ext}"
        
        if os.path.exists(filename):
            continue
            
        code_payload = {"query": CODE_QUERY, "variables": {"submissionId": sub_id}}
        code_res = requests.post(URL, json=code_payload, headers=HEADERS).json()
        code_data = code_res.get("data", {}).get("submissionDetails", {})
        
        if code_data and "code" in code_data:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(code_data["code"])
            print(f"Successfully saved: {filename}")

if __name__ == "__main__":
    main()
