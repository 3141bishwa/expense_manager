function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

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