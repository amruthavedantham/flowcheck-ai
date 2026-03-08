// TRY NOW BUTTON SCROLL

const tryButton = document.getElementById("tryButton");

tryButton.addEventListener("click", () => {
document.getElementById("workflow").scrollIntoView({
behavior: "smooth"
});
});



// FILE UPLOAD DISPLAY

const fileInput = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");

fileInput.addEventListener("change", () => {

if(fileInput.files.length > 0){

fileName.textContent = "Selected File: " + fileInput.files[0].name;

}

});



// ANALYZE BUTTON

const analyzeButton = document.getElementById("analyzeButton");

const uploadSection = document.getElementById("upload");
const processingSection = document.getElementById("processing");
const resultsSection = document.getElementById("results");

analyzeButton.addEventListener("click", () => {

if(fileInput.files.length === 0){

alert("Please upload a document first.");
return;

}


// hide upload

uploadSection.classList.add("hidden");


// show processing

processingSection.classList.remove("hidden");

simulateProcessing();

});




// SIMULATE AI PROCESSING

function simulateProcessing(){

const step1 = document.getElementById("step1");
const step2 = document.getElementById("step2");
const step3 = document.getElementById("step3");
const step4 = document.getElementById("step4");


setTimeout(()=>{

step1.style.color = "#245F73";

},1000);



setTimeout(()=>{

step2.style.color = "#245F73";

},2500);



setTimeout(()=>{

step3.style.color = "#245F73";

},4000);



setTimeout(()=>{

step4.style.color = "#245F73";

},5500);



setTimeout(()=>{

processingSection.classList.add("hidden");

resultsSection.classList.remove("hidden");

},7000);

}




// DOWNLOAD REPORT

const downloadBtn = document.getElementById("downloadBtn");

downloadBtn.addEventListener("click", () => {

const reportText = `
Process Gap Detection Report

Detected Gaps
--------------
1. Approval step missing before deployment
2. Testing phase not clearly defined
3. No rollback procedure included


Suggested Improvements
-----------------------
• Add QA validation stage
• Define rollback process
• Introduce approval checkpoint
`;

const blob = new Blob([reportText], {type:"text/plain"});

const url = URL.createObjectURL(blob);

const a = document.createElement("a");

a.href = url;
a.download = "process_gap_report.txt";

a.click();

URL.revokeObjectURL(url);

});