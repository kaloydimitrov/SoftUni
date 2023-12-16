const baseURL = "http://localhost:3030/jsonstore/tasks/";

const formElement = document.querySelector("form");

const loadMealsButton = document.getElementById("load-meals");
const addMealButton = document.getElementById("add-meal");
const editMealButton = document.getElementById("edit-meal");

const foodInput = document.getElementById("food");
const timeInput = document.getElementById("time");
const caloriesInput = document.getElementById("calories");

// --------------------- EDIT MEALS ---------------------
editMealButton.addEventListener("click", () => {
    const food = foodInput.value; const time = timeInput.value; const calories = caloriesInput.value;
    const mealId = formElement.dataset.mealId;

    const data = {
        food,
        calories,
        time,
        _id: mealId
    }

    fetch(`${baseURL}${mealId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then(loadMeals)
    .then(() => {
        foodInput.value = "";
        timeInput.value = "";
        caloriesInput.value = "";
        
        editMealButton.disabled = true;
        addMealButton.disabled = false;
    })
})

// --------------------- ADD MEALS ---------------------
addMealButton.addEventListener("click", () => {
    const food = foodInput.value; const time = timeInput.value; const calories = caloriesInput.value;
    
    if (food == "" || time == "" || calories == "") {
        console.log("Cannot add empty meal!");
        return;
    }

    const data = {
        food,
        calories,
        time
    }

    fetch(baseURL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then(loadMeals)
    .then(() => {
        foodInput.value = "";
        timeInput.value = "";
        caloriesInput.value = "";
    })
});

// --------------------- LOAD MEALS ---------------------
loadMealsButton.addEventListener("click", loadMeals);

function loadMeals() {
    const divList = document.getElementById("list");
    divList.innerHTML = "";

    fetch(baseURL)
        .then((res) => res.json())
        .then((meals) => {
            for (const meal of Object.entries(meals)) {
                const mealObject = meal[1];
                console.log(mealObject);

                // Creating elements
                const mealDiv = document.createElement("div");
                mealDiv.classList.add("meal");

                const heading2 = document.createElement("h2");
                heading2.textContent = mealObject.food;

                const heading3Time = document.createElement("h3");
                heading3Time.textContent = mealObject.time;

                const heading3Calories = document.createElement("h3");
                heading3Calories.textContent = mealObject.calories;

                const mealButtonsDiv = document.createElement("div");
                mealButtonsDiv.id = "meal-buttons";

                const changeButton = document.createElement("button");
                changeButton.classList.add("change-meal");
                changeButton.textContent = "Change";

                const deleteButton = document.createElement("button");
                deleteButton.classList.add("delete-meal");
                deleteButton.textContent = "Delete";

                // Appending elements
                mealButtonsDiv.appendChild(changeButton);
                mealButtonsDiv.appendChild(deleteButton);

                mealDiv.appendChild(heading2);
                mealDiv.appendChild(heading3Time);
                mealDiv.appendChild(heading3Calories);
                mealDiv.appendChild(mealButtonsDiv);

                divList.appendChild(mealDiv);

                // Adding Event Listeners to buttons
                changeButton.addEventListener("click", (e) => {
                    foodInput.value = mealObject.food;
                    timeInput.value = mealObject.time;
                    caloriesInput.value = mealObject.calories;

                    formElement.dataset.mealId = mealObject._id;

                    const mealElement = e.currentTarget.parentElement.parentElement;
                    mealElement.remove();

                    editMealButton.disabled = false;
                    addMealButton.disabled = true;
                });

                deleteButton.addEventListener("click", () => {
                    fetch(`${baseURL}${mealObject._id}`, {
                        method: "DELETE",
                    })
                    .then(loadMeals)
                });
            }
        });
}