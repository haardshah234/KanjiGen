const mypoints = document.getElementById('points');
//kanjiData

if (!localStorage.getItem('points')) {
    localStorage.setItem('points', 0);
}

function evaluate(event) {
    event.preventDefault();
    let points = parseInt(localStorage.getItem('points'));
    let pron1_ans = document.getElementById('pron1_ans').value.trim().toLowerCase();
    let mean1_ans = document.getElementById('mean1_ans').value.trim().toLowerCase();
    let pron2_ans = document.getElementById('pron2_ans').value.trim().toLowerCase();
    let mean2_ans = document.getElementById('mean2_ans').value.trim().toLowerCase();
    //alert(`P1='${pron1_ans}', m1='${mean1_ans}', P2='${pron2_ans}', m2='${mean2_ans}'`);
    //Case 1: when no p2,m2:
    if (kanjiData.pron2 == ''){
        var correct = true;
        if (kanjiData.pron1 == pron1_ans) {
            points += 10;
        }
        else {
            correct = false;
        }
        if (kanjiData.mean1 == mean1_ans) {
            points += 5;
        }
        else {
            correct = false;
        }
    }
    //Case 2: when p2,m2
    else {
        //alert(`${pron1_ans+mean1_ans} and ${pron2_ans+mean2_ans}`);
        var correct = true;
        if (kanjiData.pron1 == pron1_ans || kanjiData.pron1 == pron2_ans) {
            points += 10;
        }
        else {
            correct = false;
        }
        if (kanjiData.pron2 == pron2_ans || kanjiData.pron2 == pron1_ans) {
            points += 10;
        }
        else {
            correct = false;
        }
        if (kanjiData.mean1 == mean1_ans || kanjiData.mean1 == mean2_ans) {
            points += 5;
        }
        else {
            correct = false;
        }
        if (kanjiData.mean2 == mean2_ans || kanjiData.mean2 == mean1_ans) {
            points += 5;
        }
        else {
            correct = false;
        }
        if (kanjiData.pron1+kanjiData.mean1 == pron1_ans+mean1_ans || kanjiData.pron1+kanjiData.mean1 == pron2_ans+mean2_ans) {
            points += 0;
        }
        else {
            correct = false;
        }
        if (kanjiData.pron2+kanjiData.mean2 == pron2_ans+mean2_ans || kanjiData.pron2+kanjiData.mean2 == pron1_ans+mean1_ans) {
            points += 0;
        }
        else {
            correct = false;
        }
    }
    //mypoints.innerHTML = points;
    //alert(correct);
    localStorage.setItem('previous_correct',correct);
    localStorage.setItem('points',points);
    localStorage.setItem('character',kanjiData.character);
    localStorage.setItem('correct_p1',kanjiData.pron1);
    localStorage.setItem('correct_m1',kanjiData.mean1);
    localStorage.setItem('correct_p2',kanjiData.pron2);
    localStorage.setItem('correct_m2',kanjiData.mean2);
    localStorage.setItem('submitted_p1',pron1_ans);
    localStorage.setItem('submitted_m1',mean1_ans);
    localStorage.setItem('submitted_p2',pron2_ans);
    localStorage.setItem('submitted_m2',mean2_ans);
    setTimeout(() => {
        mypoints.innerHTML = points;
        event.target.submit();
    }, 20);
}

function clearPoints() {
    localStorage.setItem('points', 0);
    mypoints.innerHTML = localStorage.getItem('points');
}

function populate_result_board() {
    //Display the previous Kanji
    document.getElementById('previous_kanji').innerHTML = localStorage.getItem('character');
    //alert(localStorage.getItem('previous_correct'));
    if (localStorage.getItem('previous_correct') == 'true') {
        //alert(localStorage.getItem('previous_correct'));
        document.getElementById('result').style = "background-color: lightgreen; border: 3px solid green; color: green;";
        document.getElementById('feedback').innerHTML = "Good Job!";
    }
    else {
        document.getElementById('result').style = "background-color: lightpink; border: 3px solid red; color: red;"
        document.getElementById('feedback').innerHTML = "It's Okay! Better Luck next time!";
    }
    //Case1 
    if (localStorage.getItem('correct_p2') == '') {
        let p1 = localStorage.getItem('submitted_p1');
        let m1 = localStorage.getItem('submitted_m1');
        if (p1 == '') {
            p1 = '_(left blank)_';
        }
        if (m1 == '') {
            m1 = '_(left blank)_';
        }
        //alert('Here');
        document.getElementById('your_ans').innerHTML = `Pron: ${p1}, Mean: ${m1}`;
        document.getElementById('correct_ans').innerHTML = `Pron: ${localStorage.getItem('correct_p1')}, Mean: ${localStorage.getItem('correct_m1')}`;
    }
    else {
        let p1 = localStorage.getItem('submitted_p1');
        let m1 = localStorage.getItem('submitted_m1');
        let p2 = localStorage.getItem('submitted_p2');
        let m2 = localStorage.getItem('submitted_m2');
        if (p1 == '') {
            p1 = '_(left blank)_';
        }
        if (m1 == '') {
            m1 = '_(left blank)_';
        }
        if (p2 == '') {
            p2 = '_(left blank)_';
        }
        if (m2 == '') {
            m2 = '_(left blank)_';
        }
        document.getElementById('your_ans').innerHTML = `Pron: ${p1}, Mean: ${m1}<br>Pron: ${p2}, Mean: ${m2}`;
        document.getElementById('correct_ans').innerHTML = `Pron: ${localStorage.getItem('correct_p1')}, Mean: ${localStorage.getItem('correct_m1')}<br>Pron: ${localStorage.getItem('correct_p2')}, Meaning: ${localStorage.getItem('correct_m2')}<br>(Irrespective of Order)`;
    }
}

function move_result() {
    let shown = localStorage.getItem('result_shown');
    let obj = document.getElementById('result');
    if (shown == null) {
        localStorage.setItem('result_shown', true);
    }
    //alert(shown);
    if (shown == 'true') {
        obj.animate(
            [
                { transform: 'translateY(0%)' },
                { transform: 'translateY(-100%)' }
            ],
            { duration: 1000, easing: 'ease-in-out', fill: 'forwards' }
        );
        shown = false;
        localStorage.setItem('result_shown',shown);
    }
    else {
        obj.animate(
            [
                { transform: 'translateY(-100%)' },
                { transform: 'translateY(0%)' }
            ],
            { duration: 1000, easing: 'ease-in-out', fill: 'forwards' }
        );
        shown = true;
        localStorage.setItem('result_shown',shown);
    }
}
function move_filter() {
    let shown = localStorage.getItem('filter_shown');
    let obj = document.getElementById('filter_section');
    if (shown == null) {
        localStorage.setItem('filter_shown', true);
    }
    //alert(shown);
    if (shown == 'true') {
        obj.animate(
            [
                { transform: 'translateY(0%)' },
                { transform: 'translateY(-100%)' }
            ],
            { duration: 1000, easing: 'ease-in-out', fill: 'forwards' }
        );
        shown = false;
        localStorage.setItem('filter_shown',shown);
    }
    else {
        obj.animate(
            [
                { transform: 'translateY(-100%)' },
                { transform: 'translateY(0%)' }
            ],
            { duration: 1000, easing: 'ease-in-out', fill: 'forwards' }
        );
        shown = true;
        localStorage.setItem('filter_shown',shown);
    }
}

function setMode(mode) {
    event.stopPropagation();
    localStorage.setItem('mode', mode);
    //alert("Mode set to: " + mode);
    updateOnlyUptoStyle(mode);
}

function updateOnlyUptoStyle(mode) {
    let only = document.getElementById("only_box");
    let upto = document.getElementById("upto_box");

    only.classList.remove("active");
    upto.classList.remove("active");

    if (mode == 'only') {
        only.classList.add("active");
    }
    else {
        upto.classList.add("active");
    }
}

function redirectWithMode(event, element) {
    event.preventDefault();
    const mode = localStorage.getItem('mode') || 'only';
    const url = element.getAttribute('href') + '?mode=' + mode;
    window.location.href = url;
}

//const points = document.getElementById("points");
document.addEventListener('DOMContentLoaded', () => {
    let points = localStorage.getItem('points');
    mypoints.innerHTML = points;
    //Populate result board
    populate_result_board();
    document.getElementById('quiz_form').addEventListener('submit',evaluate);
    document.getElementById("points_box").addEventListener('click',clearPoints);
    const obj = document.getElementById("result");
    let shown = localStorage.getItem("result_shown");

    if (shown === "true") {
        // If it was open before, keep it open without animation
        obj.style.transform = "translateY(0%)";
    } else {
        // Default to hidden
        obj.style.transform = "translateY(-100%)";
        localStorage.setItem("result_shown", "false");
    }
    const obj2 = document.getElementById("filter_section");
    let shown2 = localStorage.getItem("filter_shown");

    if (shown2 === "true") {
        // If it was open before, keep it open without animation
        obj2.style.transform = "translateY(0%)";
    } else {
        // Default to hidden
        obj2.style.transform = "translateY(-100%)";
        localStorage.setItem("filter_shown", "false");
    }
    let mode = localStorage.getItem('mode') || null;
    updateOnlyUptoStyle(mode);
}); 