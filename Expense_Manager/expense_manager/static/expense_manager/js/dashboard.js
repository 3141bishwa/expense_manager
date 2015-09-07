console.log("Yes, javascript is loading");

$("#start").click(function() {
   console.log("Yes, the transaction was clicked.");
});

$("#numUsers").on("click", function() {
    var clickedOption = $('#numUsers').find(":selected").text();
    console.log(clickedOption);
});