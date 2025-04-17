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

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>


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

