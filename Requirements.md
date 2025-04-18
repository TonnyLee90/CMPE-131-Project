## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. requirement <should be 1 sentence that describes requirement>
2. requirement
3. requirement
4. requirement
5. requirement
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

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. non-functional: The app should be able to run on multiple platforms, including mobile devices and major browsers.
2. non-functional: The app should return recipe results within 3 seconds.

## 6. Use Case: Delete Recipe  
**implemented by:** Tonny Lee  
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

11. Edit User Profile  
- Pre-condition: User is logged in and viewing their own profile.  
- Trigger: User clicks “Edit Profile”.  
- Primary Sequence:  
1. User navigates to their profile page.  
2. User clicks “Edit Profile” button.  
3. System presents a form with current info pre-filled.  
4. User edits name, email, or password and submits the form.  
5. System validates the input.  
6. System updates the user info in the database.  
7. User is redirected back to the profile page with a success message.  
- Primary Postconditions:  
User data is updated in the system.  
- Alternate Sequence:  
1. User enters an invalid email.  
2. System displays error and does not update the profile.

12. Save Recipe (Favorites)  
- Pre-condition: User is logged in and viewing a recipe.  
- Trigger: User clicks the “Save” or “Favorite” button on a recipe.  
- Primary Sequence:  
1. User logs in and navigates to a recipe page.  
2. User clicks the “Favorite” button.  
3. System checks if recipe is already favorited.  
4. If not, system creates a favorite entry in the database.  
5. UI updates to show recipe is saved (e.g., filled heart icon).  
- Primary Postconditions:  
Recipe is added to the user's list of favorites.  
- Alternate Sequence:  
1. User clicks favorite again on a saved recipe.  
2. System removes the recipe from the favorite list.

13. View All Recipes  
- Pre-condition: None (publicly accessible).  
- Trigger: User visits the homepage or recipe list page.  
- Primary Sequence:  
1. User navigates to the homepage.  
2. System queries the database for all recipes.  
3. System renders the recipe list page.  
4. Each recipe is displayed with a preview (title, image, short description).  
- Primary Postconditions:  
All public recipes are shown to the user.  
- Alternate Sequence:  
1. No recipes exist in the database.  
2. Page displays “No recipes available” message.

14. Filter Recipes  
- Pre-condition: User is on the recipe list page.  
- Trigger: User selects a filter tag (e.g., “vegan” or “dessert”).  
- Primary Sequence:  
1. User views the recipe list.  
2. User selects a tag from the filter dropdown or buttons.  
3. System queries recipes by the selected tag.  
4. Filtered recipes are displayed on the same page.  
- Primary Postconditions:  
Only recipes matching the filter are shown.  
- Alternate Sequence:  
1. No recipes match the filter.  
2. System shows a “No results found” message.

15. Filter Recipes  
- Pre-condition: User is on the recipe list page.  
- Trigger: User selects a filter tag (e.g., “vegan” or “dessert”).  
- Primary Sequence:  
1. User views the recipe list.  
2. User selects a tag from the filter dropdown or buttons.  
3. System queries recipes by the selected tag.  
4. Filtered recipes are displayed on the same page.  
- Primary Postconditions:  
Only recipes matching the filter are shown.  
- Alternate Sequence:  
1. No recipes match the filter.  
2. System shows a “No results found” message.

