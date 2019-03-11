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

    
    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    //These are the filters for date, city,state,country,shape
    
    var filteredData = tableData.filter(person => person.datetime === inputValue);
    
    var filteredData2 = tableData.filter(person => person.city === inputValue);
    
    var filteredData3 = tableData.filter(person => person.state === inputValue);
    
    var filteredData4 = tableData.filter(person => person.country === inputValue);
    
    var filteredData5 = tableData.filter(person => person.shape === inputValue);
    
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
