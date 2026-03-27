document.addEventListener("DOMContentLoaded", function () {

console.log("JS loaded");

const tryButton = document.getElementById("tryButton");
const fileInput = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");
const analyzeButton = document.getElementById("analyzeButton");

const uploadSection = document.getElementById("upload");
const processingSection = document.getElementById("processing");
const resultsSection = document.getElementById("results");

const gapsList = document.getElementById("gapsList");
const suggestionsList = document.getElementById("suggestionsList");


// TRY BUTTON
tryButton.addEventListener("click", () => {
document.getElementById("upload").scrollIntoView({
behavior: "smooth"
});
});


// FILE NAME DISPLAY
fileInput.addEventListener("change", () => {
if(fileInput.files.length > 0){
fileName.textContent = "Selected File: " + fileInput.files[0].name;
}
});


// ANALYZE BUTTON
analyzeButton.addEventListener("click", async () => {

if(fileInput.files.length === 0){
alert("Please upload a document first.");
return;
}

const file = fileInput.files[0];

const formData = new FormData();
formData.append("file", file);


// SHOW PROCESSING SCREEN
uploadSection.classList.add("hidden");
processingSection.classList.remove("hidden");

// record start time
const startTime = Date.now();

try {

const response = await fetch("http://127.0.0.1:8000/upload", {
method: "POST",
body: formData
});

const result = await response.json();

console.log("Backend result:", result);


// calculate elapsed time
const elapsed = Date.now() - startTime;

// minimum processing time (2 seconds)
const delay = Math.max(2000 - elapsed, 0);

setTimeout(() => {

// HIDE PROCESSING
processingSection.classList.add("hidden");
resultsSection.classList.remove("hidden");

// CLEAR OLD RESULTS
gapsList.innerHTML = "";
suggestionsList.innerHTML = "";


// DISPLAY GAPS
const gaps = [
...result.missing_steps,
...result.unclear_steps,
...result.logical_issues
];

gaps.forEach(gap=>{
const li = document.createElement("li");
li.textContent = gap;
gapsList.appendChild(li);
});


// DISPLAY SUGGESTIONS
result.suggested_improvements.forEach(s=>{
const li = document.createElement("li");
li.textContent = s;
suggestionsList.appendChild(li);
});

}, delay);

}
catch(error){

console.error("Backend error:", error);
alert("Error connecting to backend");

}

});


// DOWNLOAD REPORT
const downloadBtn = document.getElementById("downloadBtn");

downloadBtn.addEventListener("click", () => {

const gaps = Array.from(gapsList.children).map(li => li.textContent);
const suggestions = Array.from(suggestionsList.children).map(li => li.textContent);

let report = "Process Gap Detection Report\n\nDetected Gaps\n--------------\n";

gaps.forEach((g,i)=>{
report += `${i+1}. ${g}\n`;
});

report += "\nSuggested Improvements\n-----------------------\n";

suggestions.forEach(s=>{
report += `• ${s}\n`;
});

const blob = new Blob([report], {type:"text/plain"});
const url = URL.createObjectURL(blob);

const a = document.createElement("a");
a.href = url;
a.download = "process_gap_report.txt";
a.click();

URL.revokeObjectURL(url);

});

});