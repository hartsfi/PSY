import requests
 
CANVAS_DOMAIN = "https://ohio.instructure.com"
TOKEN = "24063~CNm8DUMF86TR9UMQKEXVeV76BwFz4DkFQ7vTeGf6PhFFQ8ZJvvDyHyGtrBPnCtNJ"
 
headers = {
    "Authorization": f"Bearer {TOKEN}"
}
 
response = requests.get(
    f"{CANVAS_DOMAIN}/api/v1/users/self",
    headers=headers
)
 
user_data = response.json()
 
response = requests.get(
    f"{CANVAS_DOMAIN}/api/v1/courses",
    headers=headers
)
 
courses = response.json()
 
STUDENT_ID = user_data["id"]
 
for course in courses:
    COURSE_ID = course["id"]
 
    url = f"{CANVAS_DOMAIN}/api/v1/courses/{COURSE_ID}/students/submissions?student_ids[]={STUDENT_ID}"
 
 
    response = requests.get(url, headers=headers)
 
    data = response.json()
    print(data)
    print()