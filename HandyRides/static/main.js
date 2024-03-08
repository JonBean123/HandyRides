
function getCookie(c_name) {
   var i,x,y,ARRcookies=document.cookie.split(";");
   for (i=0;i<ARRcookies.length;i++){
      x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
      y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
      x=x.replace(/^\s+|\s+$/g,"");
      if (x==c_name) {
        return unescape(y);
      }
   }
}

function setCookie(c_name,value,exdays) {
   var exdate=new Date();
   exdate.setDate(exdate.getDate() + exdays);
   var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
   document.cookie=c_name + "=" + c_value;
}
// Implement getCookie and setCookie in 
// OR write another function that uses both in this file
// Call this in index.html

// Have to write a function that looks at the info inserted into your form 
// Call this function in index_view.html
function checkForm(form){
  var input1 = form.origination_city.value
  var input2 = form.origination_state.value
  var input3 = form.destination_city.value
  var input4 = form.destination_state.value
  var input5 = form.date.value
  var input6 = form.time.value
  var input7 = form.seats.value
  
  if (input1.trim() == '' &
      input2.trim() == '' &
      input3.trim() == '' &
      input4.trim() == '' & 
      input5.trim() == '' &
      input6.trim() == '' &
      input7.trim() == '' ){
    alert('Please fill out a search field')
    return false;
  }
  
  if (input1.trim() == 'Elon Musk' |
      input2.trim() == 'Elon Musk' |
      input3.trim() == 'Elon Musk' |
      input4.trim() == 'Elon Musk' |
      input5.trim() == 'Elon Musk' |
      input6.trim() == 'Elon Musk' |
      input7.trim() == 'Elon Musk'){
    alert("He's not here.")
    return false;
  }

  return true;
}

function checkCookie(){
  if(getCookie('first_visit') == 1){
    window.location.href = "/rides";
  } else {
    setCookie('first_visit', 1, 90)
  }
}
