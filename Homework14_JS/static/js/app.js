// from data.js
var tableData = data;
//console.log(tableData);
var tbody = d3.select("tbody");

// YOUR CODE HERE!

// Select the submit button
var submit = d3.select("#filter-btn");
submit.on("click", function() {
    

    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    var inputElement2 = d3.select("#datetime");
    var inputElement3 = d3.select("#datetime");
    var inputElement4 = d3.select("#datetime");
    var inputElement5 = d3.select("#datetime");
    
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    var inputValue2 = inputElement2.property("value");
    var inputValue3 = inputElement3.property("value");
    var inputValue4 = inputElement4.property("value");
    var inputValue5 = inputElement5.property("value");
//    console.log(inputValue);
//    console.log(inputValue2);
//    console.log(tableData);
    
    var filteredData = tableData.filter(person => person.datetime === inputValue);
    
    var filteredData2 = tableData.filter(person2 => person2.city === inputValue2);
    
    var filteredData3 = tableData.filter(person3 => person3.state === inputValue);
    
    var filteredData4 = tableData.filter(person4 => person4.country === inputValue);
    
    var filteredData5 = tableData.filter(person5 => person5.shape === inputValue);
    
    console.log(filteredData);
    console.log(filteredData2);
    console.log(filteredData3);
    console.log(filteredData4);
    console.log(filteredData5);
    
    filteredData.forEach((ufoReport) => {
        var row = tbody.append("tr");
        Object.entries(ufoReport).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
    
    filteredData2.forEach((ufoReport) => {
        var row = tbody.append("tr");
        Object.entries(ufoReport).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
    
    filteredData3.forEach((ufoReport) => {
        var row = tbody.append("tr");
        Object.entries(ufoReport).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
    
    filteredData4.forEach((ufoReport) => {
        var row = tbody.append("tr");
        Object.entries(ufoReport).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
    
    filteredData5.forEach((ufoReport) => {
        var row = tbody.append("tr");
        Object.entries(ufoReport).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
    
}
)
