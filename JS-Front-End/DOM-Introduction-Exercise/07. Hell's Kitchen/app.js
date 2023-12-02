function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      let inputResturants = eval(document.querySelector("#inputs textarea").value);

      const bestResturantResult = document.querySelector("#bestRestaurant p");
      const bestWorkersResult = document.querySelector("#workers p");

      let resturantObjects = [];
      for (const resturant of inputResturants) {
         let [name, workers] = resturant.split(" - ");

         let splitWorkers = workers.split(", ");

         let averageSalary = 0;
         let bestSalary = Number.MIN_VALUE;
         let workerObjects = [];
         for (const worker of splitWorkers) {
            let [name, salary] = worker.split(" ");
            salary = Number(salary);

            workerObjects.push({ name: name, salary: salary });
            averageSalary += salary;

            if (salary > bestSalary) {
               bestSalary = salary;
            }
         }

         resturantObject = {};

         averageSalary /= workerObjects.length;
         workerObjects.sort((a, b) => b.salary - a.salary)

         resturantObject.name = name;
         resturantObject.averageSalary = averageSalary.toFixed(2);
         resturantObject.bestSalary = bestSalary.toFixed(2);
         resturantObject.workers = workerObjects;

         let nameInArray = false;

         for (let object of resturantObjects) {
            if (object.name == resturantObject.name) {
               nameInArray = true;
               object.workers = resturantObject.workers;
               object.averageSalary = resturantObject.averageSalary;
               object.bestSalary = resturantObject.bestSalary;
            }
         }

         if (!nameInArray) {
            resturantObjects.push(resturantObject);
         }
      }

      resturantObjects.sort((a, b) => b.averageSalary - a.averageSalary);

      const bestResturant = resturantObjects[0];

      let workersArray = [];
      for (const worker of bestResturant.workers) {
         workersArray.push(`Name: ${worker.name} With Salary: ${worker.salary}`);
      }

      bestResturantResult.textContent = `Name: ${bestResturant.name} Average Salary: ${bestResturant.averageSalary} Best Salary: ${bestResturant.bestSalary}`;
      bestWorkersResult.textContent = workersArray.join(" ");
   }
}