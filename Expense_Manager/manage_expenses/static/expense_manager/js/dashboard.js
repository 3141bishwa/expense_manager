/*
 * Makes an ajax request and returns all the users currently in the database
 */
$.when($.ajax("https://jkan11lg.apps.lair.io/getallusers")).done( function(data) {
      var myData = $.parseJSON(data.users);
      var userDiv = document.getElementById("users");
      for (var i = 0; i < myData.length; i++) {
        var checkBox = document.createElement("input");
        var label = document.createElement("label");
        checkBox.type = "checkbox";
        checkBox.value = myData[i];
        checkBox.name = "checks";
        userDiv.appendChild(checkBox);
        userDiv.appendChild(label);
        label.appendChild(document.createTextNode(myData[i]));
      }
});