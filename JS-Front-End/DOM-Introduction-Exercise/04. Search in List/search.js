function search() {
   let townsArray = Array.from(document.getElementById("towns").children);
   const search = document.getElementById("searchText").value;
   const resultMatches = document.getElementById("result");

   let matches = 0;

   for (let town of townsArray) {
      if (town.textContent.includes(search)) {
         town.style.textDecoration = "underline";
         town.style.fontWeight = "bold";
         matches += 1;
      }
   }

   resultMatches.textContent = `${matches} matches found`;
}