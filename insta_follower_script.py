import instaloader

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Login to Instagram
username = "username"
password = "password"

print('Logging into Instagram...')
try:
    L.login(username, password)
except Exception as e:
    print(f"Error logging in: {e}")
    exit()

print('Logged in succesfully')

# Get the profile of the logged-in user
profile = instaloader.Profile.from_username(L.context, username)

# Get the set of followers and followees
followers = set(profile.get_followers())
followees = set(profile.get_followees())

# Find the accounts you follow but who don't follow you back
non_followers = followees - followers

# Print the usernames of non-followers
print("Accounts you follow but who don't follow you back:")
for non_follower in non_followers:
    print(non_follower.username)