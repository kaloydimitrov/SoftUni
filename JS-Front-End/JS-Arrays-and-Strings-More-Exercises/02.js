function bitcoinMining(input) {
    let bitcoins = 0;
    let totalMoney = 0;
    let dayFirstBitcoin = 0;

    for (let day = 1; day <= input.length; day++) {
        let dailyGold = input[day - 1];

        if (day % 3 == 0) {
            dailyGold *= 0.70;
        }

        totalMoney += dailyGold * 67.51;

        if (totalMoney >= 11949.16) {
            if (bitcoins == 0) {
                dayFirstBitcoin = day;
            }

            while (totalMoney >= 11949.16) {
                totalMoney -= 11949.16;
                bitcoins += 1;
            }
        }
    }

    console.log(`Bought bitcoins: ${bitcoins}`);

    if (bitcoins >= 1) {
        console.log(`Day of the first purchased bitcoin: ${dayFirstBitcoin}`);
    }

    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`);
}

bitcoinMining([3124.15, 504.212, 2511.124]);