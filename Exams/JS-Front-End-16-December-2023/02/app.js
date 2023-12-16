window.addEventListener("load", solve);

function solve() {
    const expenseType = document.getElementById("expense");
    const amount = document.getElementById("amount");
    const date = document.getElementById("date");

    const addButton = document.getElementById("add-btn");
    const deleteButton = document.querySelector(".delete");

    addButton.addEventListener("click", () => {
        if (expenseType.value == "" || amount.value == "" || date.value == "") {
            console.log("Expense, amount, or date cannot be empty!");
            return;
        }

        const ulPreviewList = document.getElementById("preview-list");

        ulPreviewList.innerHTML = `
            <li class="expense-item">
              <article>
                <p>Type: ${expenseType.value}</p>
                <p>Amount: ${amount.value}$</p>
                <p>Date: ${date.value}</p>
              </article>
              <div class="buttons">
                <button class="btn edit">edit</button>
                <button class="btn ok">ok</button>
              </div>
            </li>
            `;

        const editButton = document.querySelector(".buttons .edit");
        const okButton = document.querySelector(".buttons .ok");

        editButton.addEventListener("click", () => {
            let firstPValue = ulPreviewList.getElementsByTagName("p")[0].textContent;
            let secondPValue = ulPreviewList.getElementsByTagName("p")[1].textContent;
            let thirdPValue = ulPreviewList.getElementsByTagName("p")[2].textContent;

            const pureExpense = firstPValue.split("Type: ")[1];
            const pureAmount = secondPValue.split("Amount: ")[1].slice(0, -1);
            const pureDate = thirdPValue.split("Date: ")[1];

            ulPreviewList.innerHTML = "";
            expenseType.value = pureExpense;
            amount.value = pureAmount;
            date.value = pureDate;

            addButton.disabled = false;
        });

        okButton.addEventListener("click", () => {
            const liExpenseItem = document.querySelector(".expense-item");
            const divButtons = liExpenseItem.querySelector(".buttons");
            divButtons.remove();

            const ulExpensesList = document.querySelector("#expenses-list");
            

            console.log(liExpenseItem, ulExpensesList);
            ulExpensesList.appendChild(liExpenseItem);

            ulPreviewList.innerHTML = "";

            addButton.disabled = false;
        });

        expenseType.value = ""; amount.value = ""; date.value = "";
        addButton.disabled = true;
    });

    deleteButton.addEventListener("click", () => {
        const ulExpensesList = document.querySelector("#expenses-list");
        const selectedExpenseItem = ulExpensesList.querySelector(".expense-item");

        if (selectedExpenseItem) {
            selectedExpenseItem.remove();
        }

        const ulPreviewList = document.getElementById("preview-list");
        ulPreviewList.innerHTML = "";

        addButton.disabled = false;
    });
}