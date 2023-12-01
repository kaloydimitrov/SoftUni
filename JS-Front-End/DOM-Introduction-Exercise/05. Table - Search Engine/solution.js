function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const bodyElements = document.querySelectorAll("tbody tr");
      const inputSearch = document.getElementById("searchField");

      for (let td of bodyElements) {
         td.classList.remove("select");

         if (inputSearch.value != "" && td.innerHTML.includes(inputSearch.value)) {
            td.className = "select";
         }
      }

      inputSearch.value = "";
   }
}