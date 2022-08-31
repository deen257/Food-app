document.addEventListener("DOMContentLoaded", function () {
  const search_btn = document.getElementById("search-btn");
  const meal_List = document.getElementById("meal");
  const meal_details_content = document.querySelector(".meal-details-content");
  const recipe_close = document.getElementById("recipe-close-btn");

  // event listener
  search_btn.addEventListener("click", get_meals);
  meal_List.addEventListener("click", get_recipe);
  recipe_close.addEventListener("click", () => {
    meal_details_content.parentElement.classList.remove("showRecipe");
  });

  function get_meals() {
    let search = document.getElementById("search-input").value.trim();
    console.log(search);
    fetch(`https://www.themealdb.com/api/json/v1/1/filter.php?i=${search}`)
      .then((response) => response.json())
      .then((data) => {
        let html = "";
        console.log(data.meals);
        if (data.meals) {
          data.meals.forEach((meal) => {
            html += `
                       <div class="meal-item" data-id = "${meal.idMeal}">
                            <div class="meal-img">
                                <img src="${meal.strMealThumb}" alt="food">
                            </div>
                            <div class="meal-name">
                                <h3>${meal.strMeal}</h3>
                                <a href="#" class="recipe-btn">Get Recipe</a>
                            </div>
                        </div>
                    `;
          });
          meal_List.classList.remove("notFound");
        } else {
          meal_List.classList.add("notFound");
          html = "Sorry, we couldn't find a meal.";
        }
        meal_List.innerHTML = html;
      });
  }

  function get_recipe(e) {
    e.preventDefault;
    console.log(e.target);
    if (e.target.classList.contains("recipe-btn")) {
      let mealiteam = e.target.parentElement.parentElement;
      fetch(
        `https://www.themealdb.com/api/json/v1/1/lookup.php?i=${mealiteam.dataset.id}`
      )
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          meal = data.meals[0];
          console.log(meal);
          let html = `
                    <div class="meal-details-content">
                        <h2 class = "recipe-title">${meal.strMeal}</h2>
                            <p class="recipe-category">${meal.strCategory}</p>
                        <div class= " recipe-instrct">
                                    <h3>Instrctions:</h3>
                                    <p>${meal.strInstructions}</p>
                                </div>
                                <div class="recipe-meal-img">
                                    <img src="${meal.strMealThumb}" alt="">
                                </div>
                                <div>
                            <a href="${meal.strYoutube}" target="_blank">Watch Video</a>
                        </div>
                    </div>
                `;
          meal_details_content.innerHTML = html;
          meal_details_content.parentElement.classList.add("showRecipe");
        });
    }
  }
});
