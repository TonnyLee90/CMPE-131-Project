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
11. requirement
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. non-functional
2. non-functional

## 6. Use Case: Delete Recipe  
**impemented by:** Tonny Lee  
**Pre-condition:** The user has logged in and the recipe's author is the current logged-in user.  
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
**impemented by:** Tonny Lee  
**Pre-condition:** User is on the home page.  
**Trigger:** User clicks the “View” button below a recipe.  
**Primary Sequence:**  
- User selects a recipe to review on the home page.  
- System displays the details of the recipe including author, title, ingredients, instructions, and date. 
- User views the recipe.

**Primary Postconditions:**  
- User can view and optionally copy recipe details.

**Alternate Sequence:**  
- User selects a deleted recipe
- System prompts the user that the recipe has been deleted. Please refresh the page.

## 8. Use Case: Rate Recipe  
**impemented by:** Tonny Lee  
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
**impemented by:** Tonny Lee  
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
**impemented by:** Tonny Lee  
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



