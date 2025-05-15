# Functional Requirements Descriptions
1. User Registration: Allows a visitor to create an account by providing a username, email, and password.
2. User Login: Registered users can log in using their email and password.
3. User Logout: Logged-in users can securely log out of their account.
4. Create Recipe: Logged-in users can add new recipes including a title, description, ingredients, and instructions.
5. Edit Recipe: Registered users can update recipes they previously created.
6. Delete Recipe: This function allows logged-in users to delete their own recipes.
7. View Recipe: This function allows any user to view detailed information about a selected recipe.
8. Search Recipe: This function allows logged-in users to rate a recipe from 1 to 5 stars.
9. Rate Recipe: This function allows users to search for recipes by title or ingredient keywords.
10. Comment on Recipe: This function allows logged-in users to submit text comments on a recipe.
11. View User Profile: This function allows logged-in users to view their own profile, including all recipes they have submitted.
12. Edit User Profile: This function allows logged-in users to update their profile information such as display name, email, or password.
13. Save Recipe (Favorites): This function allows logged-in users to save or "favorite" recipes to easily access them later.
14. View All Recipes: This function allows any user to view a complete list of all available recipes on the homepage or main recipe list page.
15. Filter Recipes: This function allows users to filter recipes based on specific tags such as 'vegan', 'dessert', or other categories.
---------------
## Extra Functional Requirements Descriptions
16. View My Recipes: This function allows the user to view a complete list of their own recipes.
17. View all saved recipes: This function allows the user to view a complete list of the saved recipes.
18. Copy link: This function allows the user to copy the link of the recipe.

# Non-functional Requirements 
1. non-functional: The app should be able to run on multiple platforms, including mobile devices and major browsers.
2. non-functional: The app should return recipe results within 3 seconds.
3. non-functional: The app should secure and encode the users' password by Bcrypt Hashing

# Functional Requirements

## 1. Use case: User Registration
**implemented by:** Sergio Quispe 
**Actors:** User, System  
**Pre-condition:** The user is not registered, the user navigates to “home/registration” endpoint
**Trigger:** The user is at the Registration endpoint

**Primary Sequence:**  
- The website displays a registration form with the following fields: username, email and password
- The new user fills out all the required fields
- The user click the “submit” button
- The system validates the content of the fields 
- The system saves the information on the database  

**Primary Postconditions:**  
- The system displays a confirmation, the user is redirected to /home/profile endpoint.     

**Alternate Sequence:**  
- The system does not validate the content on the fields 
- The system displays an error prompting the user to complete the form fields

## 2.User case: User Login
**implemented by:** Sergio Quispe 
**Actors:** User, System  
**Pre-condition:** The user is registered. The user's email and password are stored in the system's database.
**Trigger:** The user navigates to the /home/login endpoint.

**Primary Sequence:**  
- The system displays a login form with email and password fields.
- The user enters their email and password.
- The user clicks the “Submit” button.
- The system checks that both fields have input.
- The system compares the provided credentials with those stored in the database.
- If the credentials match, the system logs the user in.

**Primary Postconditions:**  
- The user is redirected to the /home/profile endpoint.

**Alternate Sequence:**  
- If the form is incomplete, the system displays an error prompting the user to complete all fields.
- The email or password is incorrect.
- The system displays an error prompting the user to try again.

## 3. Use Case: User Logout
**implemented by:** Sergio Quispe  
**Actors:** User, System  
**Pre-condition:** The user is registered and logged in. The user is on the “home/profile” endpoint
**Trigger:** The user clicks the "Logout" button.

**Primary Sequence:**  
- The user clicks the "Logout" button.
- The system ends the user's session.
- The system redirects the user to the homepage or login screen.

## 4. Use Case: Create Recipe
**implemented by:** Sergio Quispe 
**Actors:** User, System  
**Pre-condition:** The user has an account and is logged in
**Actors:** User,System
**Trigger:** The user navigates to the /home/create-recipe endpoint.

**Primary Sequence:**  
- The system displays a form with fields for title, description, ingredients, and instructions.
- The user fills in the form.
- The user clicks the “Submit” button.
- The system validates the input.

**Primary Postconditions:**  
- If valid, the system saves the recipe to the database and displays a confirmation message.

**Alternate Sequence:**  
- The input fails validation.
- The system displays an error prompting the user to correct or complete the form.

## 5. Use Case: Edit Recipe
**implemented by:** Sergio Quispe 
**Actors:** User, System 
**Pre-condition:** The user has an account and is logged in, the user is on their profile page. 
**Trigger:** The user selects the “Edit” option for a recipe from their list.

**Primary Sequence:**  
- The system redirects the user to the /home/recipe/edit endpoint.
- The system pre-fills the form with the existing title, description, ingredients, and instructions.
- The user modifies the desired fields.
- The user clicks the “Submit” button.
- The system checks that all fields are filled.
**Primary Postconditions:**  
- If valid, the system updates the recipe in the database and displays a success message.
- The system redirects the user back to /home/profile.

**Alternate Sequence:**  
- If invalid, some fields are incomplete.
- The system prompts the user to fill in all required fields.

## 6. Use Case: Delete Recipe  
**implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** The user has logged in, and the recipe's author is the current logged-in user.
**Trigger:** The user clicks “Delete” button.  
**Primary Sequence:**  
- User selects a recipe  
- User clicks the “Delete” button  
- System prompts a warming to user asking if the user wants to delete the post  
- User clicks “yes” to confirm deletion.  

**Primary Postconditions:**  
- If confirmed, the recipe is deleted.
- User can’t see the recipe on any page.

**Alternate Sequence:**  
- System loses connection.  
- System displays an error message: "Unable to delete recipe. Please try again later."  
- System redirect user back to the recipe page

## 7. Use Case: View Recipe    
**implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** User is on the home page. 
**Trigger:** User clicks the “View” button below a recipe.  
**Primary Sequence:**  
- User selects a recipe to review on the home page.  
- System displays the recipe details, including author, title, ingredients, instructions, and date. 
- User views the recipe.

**Primary Postconditions:**  
- User can view and optionally copy recipe details.

**Alternate Sequence:**  
- User selects a deleted recipe
- System prompts the user that the recipe has been deleted. Please refresh the page.

## 8. Use Case: Rate Recipe  
**implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** User has logged in and on the home page. 
**Trigger:** Click “Rate” button.    
**Primary Sequence:**  
- Users select a recipe
- System displays the recipe
- User clicks “Rate” button
- System displays a rating interface
- User selects a star rating
- User clicks the “Submit” button
- System prompts that “Review has been posted.”

**Primary Postconditions:**  
- User can see their ranking
- System shows a updating ranking result

**Alternate Sequence:**  
- User submits with 0 stars
- System displays an error message to the user to select at least 1 star.

## 9. Use Case: Search Recipe  
**implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** User has logged in and on the home page.
**Trigger:** User clicks “Search” button. 
**Primary Sequence:**  
- User clicks “Filter” button
- User enters a title keyword
- System displays all recipes that have the keyword in their title
-	User enters ingredient keywords
- System displays all recipes matching keywords in their title and ingredients.

**Primary Postconditions:**  
- System displays all the recipes including key words in title and ingredient.

**Alternate Sequence:**  
- User enters invalid input in search field.
- System prompts the user to enter a valid input.  

## 10. Use Case: Comment on Recipe  
**implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** The user has logged in and the recipe's author is the current logged-in user.  
**Trigger:** User clicks the “Comment” field.  
**Primary Sequence:**  
- User enters comment text
- User clicks “Comment” button to submit
- System prompts the user that “comment posted successfully!”

**Primary Postconditions:**  
- User can see their own comment under the recipe.

**Alternate Sequence:**  
- User enters too many words and exceeds the system’s word limit.
- The system displays an error message to the user.
- The system prompts the user to comment again.

## 11. Edit User Profile  
**implemented by:** William Nguyen  
**Actors:** User, System  
**Pre-condition:** User is logged in and viewing their own profile.  
**Trigger:** User clicks “Edit Profile”.  
**Primary Sequence:** 
- User navigates to their profile page.  
- User clicks “Edit Profile” button.  
- System presents a form with current info pre-filled.  
- User edits name, email, or password and submits the form.  
- System validates the input.  
- System updates the user info in the database.  
- User is redirected back to the profile page with a success message.

**Primary Postconditions**
- User data is updated in the system.

**Alternate Sequence:**  
- User enters an invalid email.  
- System displays error and does not update the profile.

## 12. Save Recipe (Favorites)  
**implemented by:** William Nguyen  
**Actors:** User, System  
**Pre-condition:** User is logged in and viewing a recipe.  
**Trigger:** User clicks the “Save” or “Favorite” button on a recipe.  
**Primary Sequence:**  
- User logs in and navigates to a recipe page.  
- User clicks the “Favorite” button.  
- System checks if recipe is already favorited.  
- If not, system creates a favorite entry in the database.  
- UI updates to show recipe is saved (e.g., filled heart icon).
  
**Primary Postconditions:**  
- Recipe is added to the user's list of favorites. 

**Alternate Sequence:** 
- User clicks favorite again on a saved recipe.  
- System removes the recipe from the favorite list.

## 13. View All Recipes  
**implemented by:** William Nguyen  
**Actors:** User, System  
**Pre-condition:** None (publicly accessible).  
**Trigger:** User visits the homepage or recipe list page.  
**Primary Sequence:**  
- User navigates to the homepage.  
- System queries the database for all recipes.  
- System renders the recipe list page.  
- Each recipe is displayed with a preview (title, image, short description).

**Primary Postconditions:**  
- All public recipes are shown to the user.  

**Alternate Sequence:**  
- No recipes exist in the database.  
- Page displays “No recipes available” message.

## 14. Filter Recipes  
**implemented by:** William Nguyen  
**Actors:** User, System  
**Pre-condition:** User is on the recipe list page.  
**Trigger:** User selects a filter tag (e.g., “vegan” or “dessert”).  
**Primary Sequence:**  
- User views the recipe list.  
- User selects a tag from the filter dropdown or buttons.  
- System queries recipes by the selected tag.  
- Filtered recipes are displayed on the same page.

**Primary Postconditions:**  
- Only recipes matching the filter are shown.
  
**Alternate Sequence:**  
- No recipes match the filter.  
- System shows a “No results found” message.

## 15. Filter Recipes  
**implemented by:** William Nguyen  
**Actors:** User, System  
**Pre-condition:** User is on the recipe list page.  
**Trigger:** User selects a filter tag (e.g., “vegan” or “dessert”).  
**Primary Sequence:**  
- User views the recipe list.  
- User selects a tag from the filter dropdown or buttons.  
- System queries recipes by the selected tag.  
- Filtered recipes are displayed on the same page.

**Primary Postconditions:**  
- Only recipes matching the filter are shown.
 
**Alternate Sequence:**  
- No recipes match the filter.  
- System shows a “No results found” message.

## 16. Use Case: View My Recipes  
**Implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** User has logged in
**Trigger:** User clicks “My Recipes” button.  
**Primary Sequence:**  
- User clicks “My Recipes” button  
- System retrieves all recipes created by the user  
- System displays the list of the user's recipes  

**Primary Postconditions:**  
- System displays all recipes created by the user.

**Alternate Sequence:**  
- No recipes found.  
- System displays a message: “You have not created any recipes yet.”  

---

## 17. Use Case: View All Saved Recipes  
**Implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** User has logged in
**Trigger:** User clicks “My Favorites” button.  
**Primary Sequence:**  
- User clicks “Saved Recipes” button  
- System retrieves all recipes saved by the user  
- System displays the list of saved recipes  

**Primary Postconditions:**  
- System displays all recipes saved by the user.

**Alternate Sequence:**  
- No saved recipes found.  
- System displays a message: “You have no saved recipes.”  

---

## 18. Use Case: Copy Link  
**Implemented by:** Tonny Lee  
**Actors:** User, System  
**Pre-condition:** User is on the home page.  
**Trigger:** User clicks the “Copy Link” icon or button.  
**Primary Sequence:**  
- User clicks the “Copy Link” icon/button next to a recipe  
- System copies the recipe’s URL to the clipboard  
- System displays a confirmation message: Link copied!

**Primary Postconditions:**  
- Recipe link is successfully copied to the clipboard.

**Alternate Sequence:**  
- Clipboard copy fails.  
- System displays an error message: Unable to copy link. Please try again.

