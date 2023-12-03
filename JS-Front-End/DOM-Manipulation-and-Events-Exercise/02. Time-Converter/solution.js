function attachEventsListeners() {
    const daysInput = document.getElementById("days");
    const hoursInput = document.getElementById("hours");
    const minutedInput = document.getElementById("minutes");
    const secondsInput = document.getElementById("seconds");

    console.log(daysInput, hoursInput, minutedInput, secondsInput);

    document.getElementById("daysBtn").addEventListener("click", (e) => {
        const currentValue = daysInput.value;

        hoursInput.value = currentValue * 24;
        minutedInput.value = currentValue * 24 * 60;
        secondsInput.value = currentValue * 24 * 60 * 60;
    });
    document.getElementById("hoursBtn").addEventListener("click", (e) => {
        const currentValue = hoursInput.value;

        daysInput.value = currentValue / 24;
        minutedInput.value = currentValue * 60;
        secondsInput.value = currentValue * 60 * 60;
    });
    document.getElementById("minutesBtn").addEventListener("click", (e) => {
        const currentValue = minutedInput.value;

        daysInput.value = currentValue / 1440;
        hoursInput.value = currentValue / 60;
        secondsInput.value = currentValue * 60;
    });
    document.getElementById("secondsBtn").addEventListener("click", (e) => {
        const currentValue = secondsInput.value;

        daysInput.value = currentValue / 86400;
        hoursInput.value = currentValue / 3600;
        minutedInput.value = currentValue / 60;
    });
}