function formatGrade(grade) {
    gradeWord = '';

    if (grade < 3) {
        gradeWord = "Fail";
    }
    else if (grade >= 3 && grade < 3.50) {
        gradeWord = "Poor";
    }
    else if (grade >= 3.50 && grade < 4.50) {
        gradeWord = "Good";
    }
    else if (grade >= 4.50 && grade < 5.50) {
        gradeWord = "Very good";
    }
    else if (grade >= 5.50) {
        gradeWord = "Excellent";
    }

    console.log(`${gradeWord} (${grade.toFixed(2)})`);
}

formatGrade(4.50);